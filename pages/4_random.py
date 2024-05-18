import streamlit as st
import random

if st.button('버튼'):
    player = random.randrange(1, 4)
    if player == 1:
        st.write('오늘의 선수1')
        st.write('선수1 정보')
    elif player == 2:
        st.write('오늘의 선수2')
        st.write('선수2 정보')
    elif player == 3:
        st.write('오늘의 선수3')
        st.write('선수3 정보')