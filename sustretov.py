#Сустретов И.С., группа ПИ-4см
#Вариант #3. Используя приложенный файл data.csv, вывести имя, возраст, класс билета мужчин указанного возраста (от 30 до 60 лет).

import streamlit as st


def sustretov_code():
    st.subheader("Сустретов И.С., группа ПИ4-см.")
    st.success("Работа с библиотекой Streamlit, вариант 3")
    st.success("Пассажиры \"Титаника\", мужчины от 30 до 60 лет, вывод имени, возраста, класса билета в указанном диапазоне возраста")
    age_range = st.slider('Укажите диапазон возраста пассажиров', 30.0, 60.0, (35.0, 55.0), 0.5)
    min_age = age_range[0]
    max_age = age_range[1]
    pass_data = {}
    with open("data.csv", mode="r") as file:
        next(file)
        for line in file:
            cur_str = line.split(",")
            if cur_str[5] == "male":  # отбираем данные по критериям согласно задания
                if not cur_str[6]:  # проверка на пустое поле возраста в файле данных
                    continue
                else:
                    cur_age = float(cur_str[6])
                    if cur_age >= float(min_age) and cur_age <= float(max_age):
                        # формируем нужные данные для файла результата согласно варианта
                        name = cur_str[3] + " " + cur_str[4]
                        pass_class = cur_str[2]
                        pass_data[name] = {"Возраст": cur_age, "Класс билета": pass_class}
    st.table(pass_data)
