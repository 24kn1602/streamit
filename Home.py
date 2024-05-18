#home.py
#가상환경 // 패키지 안 꼬이려고
# 파이썬 버전 독자적으로 쓰려고
# 프로젝트별 독립된 환경에서 쓰려고
# 멀티페이지 구성
# 폴더이름은 무조건 pages
# session_state
# st.camera_input 

#$ pip install streamlit 
#$ streamlit run 파일명.py

import streamlit as st
from PIL import Image

st.title('축구 소개 페이지')
st.write('11vs11로 발을 써서 공을 골대에 많이 넣으면 이김')
img = Image.open('data/sports.jpg')

st.image(img)