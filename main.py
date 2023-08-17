import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目':[1, 2, 3, 4],
    '2列目':[10, 20, 30, 40]
})

#st.write(df)

#st.dataframe(df)

#st.dataframe(df, width=500, height=500)

#st.dataframe(df.style.highlight_max(axis=0), width=500, height=500)

st.table(df.style.highlight_max(axis=0))


df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

st.text('Mai Takiguchi')

st.caption('This is a string that explains something above.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')


code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')



st.write("This is some text.")

st.slider("This is a slider", 0, 100, (25, 75))

#st.divider()  # 👈 Draws a horizontal rule

st.write("This text is between the horizontal rules.")

#st.divider()  # 👈 Another horizontal rule
















#↓MarkDown
#"""
# # 章
# ## 節
# ### 項

#```python
#import streamlit as st
#import numpy as np
#import pandas as pd
#```
#"""








#st.markdown('Streamlit is **_really_ cool**.')
#st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
#st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")



#st.json({
#    'foo': 'bar',
#    'baz': 'boz',
#    'stuff': [
#        'stuff 1',
#        'stuff 2',
#        'stuff 3',
#        'stuff 5',
#    ],
#})

