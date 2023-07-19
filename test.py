import streamlit as st
import pandas as pd
view = [100,150,30]
view

st.write('# Hello')
st.write('## hi')
st.write('### bar chart')


st.bar_chart(view)
sview = pd.Series(view)
sview