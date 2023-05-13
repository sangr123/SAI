import streamlit as st
import pandas as pd

# df = pd.read_excel("C:/temp/streamlit/gpt.xlsx", index_col=0)
df = pd.read_excel("gpt_p.xlsx", index_col=0)

# 타이틀 출력
st.title("🏢 기업 토픽 🏢")
st.markdown("&nbsp;\n\n\n\n&nbsp;")
# 사이드바 타이틀
st.sidebar.title("기업 검색🔍")

# 검색어 입력 받기
search_query = st.sidebar.text_input("검색")

# 검색어를 메인에 출력
if search_query:
    st.header(search_query)
# str1 = "2020"
# str2 = "2021"
# str3 = "2022"

matching_columns20 = [col for col in df.columns if search_query + "2020" in col]
matching_columns21 = [col for col in df.columns if search_query + "2021" in col]
matching_columns22 = [col for col in df.columns if search_query + "2022" in col]

# search_query_2020 = search_query + str1
# search_query_2021 = search_query + str
# search_query_2022 = search_query + "2022"

# 레이아웃 만들기
# 3개의 열을 생성
col1, col2, col3 = st.columns((3,3,3))

# 첫 번째 열에 내용 추가
with col1:
    st.header("📋2020")
    if not search_query:
        st.write("검색어를 입력해주세요.")
    else:
        if not matching_columns20:
            st.write("검색 결과가 없습니다.")
        else:
            st.write(df[matching_columns20])
       

# 두 번째 열에 내용 추가
with col2:
    st.header("📋2021")
    if not search_query:
        st.write("검색어를 입력해주세요.")
    else:
        if not matching_columns21:
            st.write("검색 결과가 없습니다.")
        else:
            st.write(df[matching_columns21])

# 세 번째 열에 내용 추가
with col3:
    st.header("📋2022")
    if not search_query:
        st.write("검색어를 입력해주세요.")
    else:
        if not matching_columns22:
            st.write("검색 결과가 없습니다.")
        else:
            st.write(df[matching_columns22])


# streamlit run lay.py








