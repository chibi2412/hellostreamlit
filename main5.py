import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('Progress Bar')
'Start!!!!!!!!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
        latest_iteration.text(f'Iteration{i+1}')
        bar.progress(i+1)
        time.sleep(0.1)

'Done!!!!!!!!'


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
