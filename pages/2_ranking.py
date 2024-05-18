import streamlit as st
import pandas as pd

st.title('Hello, Streamlit!')
data = {
    'Name': ['Player1', 'Player2', 'Player3'],
    'Games_Played': [150, 200, 175],
    'Goals': [75, 110, 90],
    'Assists': [50, 85, 65]
}


df = pd.DataFrame(data)


st.dataframe(df)
st.line_chart(df)

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    if st.button('export'):
        st.write('성공')