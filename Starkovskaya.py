import streamlit as st
import pandas as pd


def count_depending_sex_and_save(dataframe, sex, survived):
    df = dataframe[(dataframe['Sex'] == sex) & (dataframe['Survived'] == survived)][['Name', 'Age', 'Pclass']]
    return df


def starkovskaya_code():
    st.write("Homework 9, Старковская Т.В., группа 4пи, 17 вариант, по заданию 2")
    st.write("Вывести имя, возраст, класс билета пассажиров, выбрав пол и спасен/нет.")
    with st.sidebar:
        with st.form(key='form'):
            sex = st.selectbox('Выберите пол', ('male', 'female'))
            survived = st.selectbox('Выживший или нет?', (0, 1))
            submit = st.form_submit_button(label='Calculate')
    if submit:
        csv = pd.read_csv('data.csv')
        st.write(count_depending_sex_and_save(csv, sex, survived))
    else:
        st.text("Для получения информации выберите, пожалуйста, пол и статус (0 - погиб, 1 - выжил)")


starkovskaya_code()
