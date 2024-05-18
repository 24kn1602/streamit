import streamlit as st
import pandas as pd

st.title('K리그1')
st.text('https://sports.daum.net/record/kl')
data = pd.read_csv('data/record2.csv')
df = pd.DataFrame(data)

st.dataframe(df)

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False


if st.session_state.logged_in:
    csv = df.to_csv(index=False, encoding='utf-8-sig').encode('utf-8-sig')
    if st.download_button('Download CSV', csv, 'ranking.csv', 'text/csv'):
        st.write('내보내기 성공')

score = df[['승점']]
st.bar_chart(score)