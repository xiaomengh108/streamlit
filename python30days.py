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
letter='p'
st.write(letter)
st.write(len(letter))
greeting = 'Hello, World!'
st.write(greeting)
st.write(len(greeting))
sentence = 'I hope you are enjoying 30 days of Python Challenge'
st.write(sentence)
multiline_string='''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
st.write(multiline_string)

first_name='Asabeneh'
last_name='Yetayeh'
space=' '
full_name=first_name+space+last_name
st.write(full_name)
st.write(len(first_name))
st.write(len(last_name))
st.write(len(first_name)>len(last_name))
st.write(len(full_name))

st.write('I hope everyone is enjoying the Python Challenge.\n Are you?')
st.write('Days\tTopics\tExercists')
st.write('Day 1\t3\t5')
st.write('Day 2\t3\t5')
st.write('Day 3\t3\t5')
st.write('Day 4\t3\t5')
st.write('This is a backslash symbol(\\)')
st.write('In every programming language it starts with \"Hello,world!\"')

radius=10
pi=3.14
area=pi*radius**2

language = 'python'
first_letter=language[0]
st.write(first_letter)

string_1 = ['Thirty','Days','of','Python']
string_1_concatenated = ' '.join(string_1) #ex.1
st.write(string_1_concatenated)
string_2=['Coding','For','All']
string_2_concatenated=' '.join(string_2)
st.write(string_2_concatenated) #ex.2
company=string_2_concatenated #ex.3
st.write(company) #ex.4
st.write(len(company)) #ex.5
st.write(company.upper()) #ex.6
st.write(company.lower()) #ex.7
st.write(company.capitalize())
st.write(company.title())
st.write(company.swapcase()) #ex.8
st.write(company[0:6]) #ex.9
st.write(company.index('Coding')) #ex.10
st.write(company.replace('Coding','Python')) #ex.11
pythonforeveryone = 'Python for Everyone'
st.write(pythonforeveryone.replace('Everyone','All')) #ex.12
st.write(company.split(' ')) #ex.13
techcompanies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
st.write(techcompanies.split(',')) #ex.14
st.write(company[0]) #ex.15
st.write(company[-1])#ex.16
st.write(company[10])#ex.17 #space
st.write(company.find('C')) #ex.20
st.write(company.rfind('F')) #ex.21
company_people='Coding For All People'
st.write(company_people.rfind('l')) #ex.22
sentence_1= 'You cannot end a sentence with because because because is a conjunction'
st.write(sentence_1.find('because')) #ex.23
st.write(sentence_1.rfind('because')) #ex.24
st.write(sentence_1[31:54]) #ex.25 & #ex.27
st.write(sentence_1.index('because')) #ex.26
st.write(company.startswith('Coding')) #ex.28
st.write(company.endswith('Coding')) #ex.29
company_space='   Coding For All      '
st.write(company_space)
st.write(company_space.strip(' ')) #ex.30
challenge='30DaysOfPython'
st.write(challenge.isidentifier())
challenge_thirty='thirty_days_of_python'
st.write(challenge_thirty.isidentifier()) #ex.31
libraries=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
results='_ '.join(libraries)
st.write(results) #ex.32
st.write('I am enjoying this challenge.\nI just wonder what is next.') #ex.33
st.write('Name\tAge\tCountry\tCity')
st.write('Asabeneh\t250\tFinland\tHelsinki') #ex.34
radius = 'radius = 10'
st.write(radius)
area= 'area = 3.14 * radius ** 2'
st.write(area)

st.header('Day 5')
empty_list=list()#q1
weekdays=['Monday','Tuesday','Wednesday','Thursday','Friday'] #q2
st.write(len(weekdays)) #q3
st.write(weekdays[0])
st.write(weekdays[2])
st.write(weekdays[4]) #q4
mixed_data_types=['Liz',36,1.73,'unmarried','New York'] #q5
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'] #q6
st.write(it_companies) #q7
st.write(len(it_companies)) #q8
st.write(it_companies[0])
st.write(it_companies[3])
st.write(it_companies[6]) #q9
it_companies[1] = 'OpenAI'
st.write(it_companies) #q10
it_companies.append('Duolingo')
st.write(it_companies) #q11
it_companies.sort()
st.write(it_companies) #q12
it_companies.insert(4,'Tencent')
st.write(it_companies) #q13




























































































































