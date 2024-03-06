import streamlit as st
from Langchain_Practice import poem_content
from streamlit_extras.buy_me_a_coffee import button

def BMC():
    button(username="silverstone", floating=True, width=221)

BMC()
st.title('인공지능 시인')
title = st.text_input('시의 주제를 입력해 주세요.')
if st.button('시 작성 요청하기'):
    with st.spinner('시 작성중...'):
        result = poem_content(title)
        st.write(result.content)
