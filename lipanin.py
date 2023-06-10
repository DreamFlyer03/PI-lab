import streamlit as st
import pandas as pd


def get_pass_list(data, sex, age_start, age_end):
    if sex == 'мужской':
        sex = 'male'
    else:
        sex = 'female'
    out_list = []
    for index, row in data.iterrows():
        if row['Survived'] == 1 and row['Sex'] == sex and age_start <= row['Age'] <= age_end:
            out_list.append(f"{row['Name']}, {row['Sex']}, {int(row['Age'])} лет")
    return out_list


def lipanin_code():
    st.header("Липанин В.А., группа ПИ4-см.")
    st.header("Лабораторная работа №9 - Работа с библиотекой Streamlit, вариант 1")
    st.subheader("Пассажиры \"Титаника\", Вывести имя и возраст спасенных детей, указав пол и возраст (от 0 до 18)")
    data = pd.read_csv('data.csv')
    sex = st.radio('Выберите пол пассажира:', ['мужской', 'женский'])
    age_start, age_end = st.slider('Выберите возраст:', 0, 18, (0, 18))
    st.table({"Спасенные пассажиры (имя, пол, возраст):": get_pass_list(data, sex, age_start, age_end)})


lipanin_code()
