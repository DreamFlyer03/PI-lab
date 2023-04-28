import streamlit as st
import pandas as pd

def Starkovskaya_code():
    st.write("Homework 9, Старковская Т.В., группа 4пи, 17 вариант, по заданию 2")
    st.write("Вывести имя, возраст, класс билета пассажиров, выбрав пол и спасен/нет.")
    with st.sidebar:
        with st.form(key='form'):
            sex = st.selectbox('Выберите пол', ('male', 'female'))
            survived = st.selectbox('Выживший или нет?', (0, 1))
            submit = st.form_submit_button(label='Calculate')
    if submit:
       csv = pd.read_csv('data.csv')
    if sex == 'male' and survived == 0:
        st.write(csv[(csv['Sex'] == 'male') & (csv['Survived'] == 0)][['Name', 'Age', 'Pclass']])
    elif sex == 'male' and survived == 1:
        st.write(csv[(csv['Sex'] == 'male') & (csv['Survived'] == 1)][['Name', 'Age', 'Pclass']])
    elif sex == 'female' and survived == 0:
        st.write(csv[(csv['Sex'] == 'female') & (csv['Survived'] == 0)][['Name', 'Age', 'Pclass']])
    elif sex == 'female' and survived == 1:
        st.write(csv[(csv['Sex'] == 'female') & (csv['Survived'] == 1)][['Name', 'Age', 'Pclass']])
