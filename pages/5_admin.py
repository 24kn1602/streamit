import streamlit as st

account = {'id':'admin','password':'qwerty'}

st.text('admin page')
inputid = st.text_input('아이디 입력')
inputpassword = st.text_input('비밀번호 입력', type='password')

if st.button('로그인'):
    if inputid == account['id'] and inputpassword == account['password']:
        st.session_state.logged_in = True
        st.write('로그인 성공')
    else:
        st.write('로그인 실패')


