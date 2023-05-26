import streamlit as st
import pandas as pd

# Создать веб-приложение, используя возможности библиотеки streamlit,
# для обработки данных пассажиров “Титаника” (файл data.csv приложен к заданию).


# 4. Вывести имена пассажиров, стоимость билета (поле Fare) которых была выше указанной.


# считывание файла через pandas (сказали, что можно)
def get_input_data_as_pd():
    csv = pd.read_csv('data.csv')
    return csv


def filter_pd_data(csv, price):
    return csv[csv['Fare'] > price]


def filter_pd_data_as_list(csv, price):
    return csv[csv['Fare'] > price]['Name']


def sukhanova_code():
    # делаем страничку пошире
    # st.set_page_config(layout="wide", page_title="Homework Суханова Н.А.")

    # заголовки + задание
    st.header("Суханова Н.А.")
    st.write("Создать веб-приложение, используя возможности библиотеки streamlit, "
             "для обработки данных пассажиров “Титаника” (файл data.csv приложен к заданию).")
    st.write("Вывести имена пассажиров, стоимость билета (поле Fare) которых была выше указанной.")

    # весь функционал в сайдбаре
    with st.sidebar:
        with st.form(key='my_form'):
            # запрос на стоимость билета
            price = st.text_input('Введите стоимость билета:', 10)

            # запрос на то, в каком формате вывести (табличка или список имен)
            result = st.radio('result as table or list', ('table', 'list'))

            # кнопка отправки
            submit = st.form_submit_button(label='Получить результат')

    # обработка нажатия кнопки
    if submit:
        csv = get_input_data_as_pd()

        # обработка варианта вывода (табличка или список имён)
        if result == 'table':
            st.write(filter_pd_data(csv, float(price)))
        else:
            st.write(filter_pd_data_as_list(csv, float(price)))

sukhanova_code()

