import streamlit as st
import math as math
import numpy as np
import pandas as pd

st.header('Day 1')
st.write(2+3)
st.write(2*3)
st.write(3-2)
st.write(3/2)
st.write(3%2)
st.write(2%3)
st.write(3//2)
st.write(3**2)
st.write(type(3.14))
st.write(type(1+3j))
print(type({3,5,8}))
print(type(['Asabeneh','Python','Finland']))

#Find an Euclidian distance between (2, 3) and (10, 8)

p1=[2,3]
p2=[10,8]
ed= math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
st.write(ed)

st.header('Day 2')
st.write('Hello, World!')
st.write(len('Hello, World!'))
print(type('Hello, World!'))
st.write(int('10'))
st.write(float('10'))
#help('False')
#help('elif')
st.write(min(20,30,40,50))
st.write(max(20,30,40,50))
st.write(sum([20,30,40,50]))
first_name = 'xiaomeng '
last_name='huang'
full_name=first_name+last_name
st.write(full_name)
country='us'
city='newyork'
is_married=False
is_true=True
is_light_on=False
st.write(first_name,last_name,country,city,is_light_on)
type(first_name)
st.write(type(is_married))
st.write(len(first_name)>len(last_name))
num_one=5
num_two=4
total=num_one+num_two
st.write(total)
diff=num_one-num_two
product=num_one*num_two
division=num_one/num_two
remainder=num_one%num_two
st.write(remainder)
exp=pow(num_one,num_two)
st.write(exp)
floor_division=num_one//num_two
st.write(floor_division)
area_of_circle=30**2*np.pi
st.write('area_of_circle:', area_of_circle)
circum_of_circle = 2*30*np.pi
st.write('circum_of_circle:', circum_of_circle)

st.header('Day 3')
base=st.text_input('Enter base:')
height=st.text_input('Enter height:')
if height:
    st.write("The area of the triangle is:",int(base)*int(height)/2)

side_a=st.text_input('Enter side a:')
side_b=st.text_input('Enter side b:')
side_c=st.text_input('Enter side c:')
if side_c:
    st.write("The perimeter of the triangle",int(side_a)+int(side_b)+int(side_c))

length=st.text_input('Enter length:')
width=st.text_input('Enter width:')
if width:
    st.write("The perimeter is:",int(length)*int(width)*2)

hours=st.text_input('Enter hours:')
rate_per_hour=st.text_input('Enter rate per hour:')
if rate_per_hour:
    st.write("Your weekly earning is:",int(hours)*int(rate_per_hour))

number_of_years=st.text_input('Enter number of years you have lived:')
if number_of_years:
    st.write("You have lived for",int(number_of_years)*3153600,"seconds")

df = pd.DataFrame({
    'col1':[1,2,3,4,5],
    'col2':[1,1,1,1,1],
    'col3':[1,2,3,4,5],
    'col4':[1,4,9,16,25],
    'col5':[1,8,27,64,125]
     })
st.write(df)

st.header('Day 4')












































