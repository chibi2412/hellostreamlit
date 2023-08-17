import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

#st.write('DataFrame')

st.write('Interactive Widgets')

#if st.checkbox('Show Image'):

option = st.text_input('あなたの趣味を教えて下さい。')
#option = st.sidebar.text_input('あなたの趣味を教えて下さい。')
'あなたの趣味：', option, 'です。'

condition = st.slider('あなたの今の調子は？', 0, 100, 50)
#condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

'コンディション：', condition

#option = st.sidebar.selectbox(
option = st.selectbox(
    'あなたが好きな数字を教えてください、',
    list(range(1, 10))
)

'あなたの好きな数字は、',option, 'です。'

    # img = Image.open('1.jpg')
    # st.image(img, caption='Masaya Takiguchi', use_column_width=True)
