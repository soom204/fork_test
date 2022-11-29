import streamlit as st
import numpy as np
import pandas as pd

st.title('제목')
st.header('헤더')
st.subheader('서브헤더')
st.text('그냥 문자열!')

code = "print('hello! python')"

st.code(code)

st.markdown('''
# 큰 제목

**진하게**
''')

file_name = './jjanggu_list.csv'

df = pd.read_csv(file_name, encoding='UTF-8')

st.dataframe(df)
