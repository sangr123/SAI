import streamlit as st
import pandas as pd

df = pd.read_excel("gpt_p.xlsx", index_col=0)
df_cnum = pd.read_excel("cname.xlsx", index_col=0)

# 타이틀 출력
st.title("🏢 기업 토픽 🏢")

st.subheader("너 뭐 돼?🤷🏻‍♀️")

#공백 추가
st.markdown("&nbsp;\n\n\n\n&nbsp;")

# 사이드바 타이틀
st.sidebar.title("기업 검색🔍")

# 검색어 입력 받기
search_query = st.sidebar.text_input("검색")

# 검색어를 메인에 출력
if search_query:
    st.header(search_query)
else:
    st.subheader("검색어를 입력해 주세요.")

matching_columns20 = [col for col in df.columns if search_query + "2020" in col]
matching_columns21 = [col for col in df.columns if search_query + "2021" in col]
matching_columns22 = [col for col in df.columns if search_query + "2022" in col]


# 레이아웃 만들기
# 3개의 열을 생성
col1, col2, col3 = st.columns(3)

# 첫 번째 열에 내용 추가
with col1:
    st.header("📋 2020")
    if not search_query:
        st.write()
    else:
        if not matching_columns20:
            st.write("검색 결과가 없습니다.")
        else:
            st.write(df[matching_columns20])
       
# 두 번째 열에 내용 추가
with col2:
    st.header("📋 2021")
    if not search_query:
        st.write()
    else:
        if not matching_columns21:
            st.write("검색 결과가 없습니다.")
        else:
            st.write(df[matching_columns21])

# 세 번째 열에 내용 추가
with col3:
    st.header("📋 2022")
    if not search_query:
        st.write()
    else:
        if not matching_columns22:
            st.write("검색 결과가 없습니다.")
        else:
            st.write(df[matching_columns22])

#공백 추가
st.markdown("&nbsp;\n\n\n\n&nbsp;")


######################
##### 그래프 출력 #####
######################


from pykrx import stock
import plotly.graph_objects as go
from datetime import datetime
from dateutil.relativedelta import relativedelta


st.header("📊 거래 정보")

now = datetime.now()
current_date = now.strftime("%Y%m%d") # 현재 날짜

old = now + relativedelta(months=-6)
previous_date = old.strftime("%Y%m%d") # 6개월 전 날짜

## 레이아웃 만들기
# 2개의 열을 생성
col1, col2 = st.columns(2)

# 첫 번째 열에 주가 그래프 추가
with col1:   
    if not search_query:
        st.write()
    else:
        if not matching_columns22:
            st.write("검색 결과가 없습니다.")
        else:
            cnum = df_cnum.loc[search_query , '종목코드']
            
            # 최근 6개월 주가 데이터 가져오기
            df_stock = stock.get_market_ohlcv_by_date(previous_date, current_date, cnum)
            
            # 주가 그래프 그리기
            fig_price = go.Figure()
            fig_price.add_trace(go.Scatter(x=df_stock.index, y=df_stock['종가'], name='종가'))
            fig_price.update_layout(title='최근 6개월 주가')
            st.plotly_chart(fig_price)
            st.write("종합 정보")
            st.write(df_stock)
          
# 두 번째 열에 거래량 그래프 추가
with col2:
    if not search_query:
        st.write()
    else:
        if not matching_columns22:
            st.write("검색 결과가 없습니다.")
        else:
            # 거래량 그래프 그리기
            fig_volume = go.Figure()
            fig_volume.add_trace(go.Bar(x=df_stock.index, y=df_stock['거래량'], name='거래량'))
            fig_volume.update_layout(title='최근 6개월 거래량')
            st.plotly_chart(fig_volume)
