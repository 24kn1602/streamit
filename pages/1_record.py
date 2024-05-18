import streamlit as st
import pandas as pd

st.title('역대 월드컵 기록')
data = pd.read_csv('data/record.csv')


df = pd.DataFrame(data)

goal = df[['골수']]

st.dataframe(df)

st.write('골 수 그래프')
st.line_chart(goal)