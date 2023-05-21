# Сустретов И.С., группа ПИ-4см. Лабораторная работа #11 Вариант #3. Используя приложенный файл data.csv,
# вывести имя, возраст, класс билета мужчин указанного возраста (от 30 до 60 лет). Создать несколько тестов для
# проверки функции выбора корректных данных


import streamlit as st

result = {}


def get_data_from_file():
    f = open("data.csv", mode="r")
    return f


#  функция, которую тестируем. на вход подаем критерии отбора, для тестов - указываем дефолтное значение по заданию
def process_data(file, min_age=30.0, max_age=60.0):
    pass_data = {}
    for line in file:
        cur_str = line.split(",")
        if cur_str[5] == "male":  # отбираем данные по критериям согласно задания
            if not cur_str[6]:  # проверка на пустое поле возраста в файле данных
                continue
            else:
                cur_age = float(cur_str[6])
                if float(min_age) <= cur_age <= float(max_age):
                    # формируем нужные данные для файла результата согласно варианта
                    name = cur_str[3] + " " + cur_str[4]
                    pass_class = cur_str[2]
                    pass_data[name] = {"Возраст": cur_age, "Класс билета": pass_class}
        else:
            continue
    return pass_data


st.header("Сустретов И.С., группа ПИ4-см.")
st.header("Лабораторная работа №9 - Работа с библиотекой Streamlit, вариант 3")
st.subheader("Пассажиры \"Титаника\", мужчины от 30 до 60 лет")
age_range = st.slider('Укажите диапазон возраста пассажиров', 30.0, 60.0, (35.0, 55.0), 0.5)
age_min = age_range[0]
age_max = age_range[1]

work_file = get_data_from_file()  # готовим информацию для обработки
result = process_data(work_file, age_min, age_max)  # отбираем нужное в нашей функции, которую будем тестировать

st.table(result)  # выводим итоговую таблицу
