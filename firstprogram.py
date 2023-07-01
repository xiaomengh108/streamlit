
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

from datetime import time, datetime
st.header('st.slider')
age=st.slider('How old are you?',0,130,25)
st.write("I'm",age,"years old")

st.subheader('Range slider')
values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0,75.0))
st.write('Values:', values)

st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

st.subheader('Datatime slider')
start_time=st.slider(
    "when do you start?",
    value=datetime(2020,1,1,9,30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

st.header('Line chart')
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c'])
st.line_chart(chart_data)

st.header('st.selectbox')
option = st.selectbox('what is your favoirite color?',
                      ('Blue', "Red", "Green"))
st.write('Your favorite color is', option)


st.header('st.multiselect')
options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)

st.header('st.checkbox')
st.write('What would you like to order?')
icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')
if icecream:
    st.write("Great! Here's some more 🍦")
if coffee:
    st.write("Okay,here's some coffee ☕")
if cola:
    st.write("Here you go 🥤")

st.write(2+3)













