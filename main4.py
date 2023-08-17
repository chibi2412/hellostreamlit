import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('Interactive Widgets')

#left_column, right_column = st.beta_columns(2)
left_column, right_column = st.columns(2)

button = left_column.button('右カラムに文字を表示')
if button:
        right_column.write('ここは右カラム')

expander = st.expander('問い合わせ内容１')
expander.write('問い合わせ内容１の回答')
expander = st.expander('問い合わせ内容２')
expander.write('問い合わせ内容２の回答')
expander = st.expander('問い合わせ内容３')
expander.write('問い合わせ内容３の回答')
expander = st.expander('問い合わせ内容４')
expander.write('問い合わせ内容４の回答')



# option = st.text_input('あなたの趣味を教えて下さい。')
# 'あなたの趣味：', option, 'です。'

# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# #condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

# 'コンディション：', condition

# option = st.selectbox(
#     'あなたが好きな数字を教えてください、',
#     list(range(1, 10))
# )

# 'あなたの好きな数字は、',option, 'です。'

