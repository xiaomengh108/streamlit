
import streamlit as st

st.write('Hello world!')
st.write(2+3)
st.header ("st.button")
if not st.button('say hello'):
        st.write ('good bye')
else:
    st.write('why hello here')

import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')
st.write('Hello,*world!* :sunglasses:')
st.write(1234)
df=pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})
st.write(df)
st.write('Below is a DataFrame:', df, 'Above is a DataFrame.')

df2=pd.DataFrame(
    np.random.randn(200,3),
    columns=['a','b','c'])
c=alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c',color='c', tooltip=['a','b','c'])
st.write(c)












