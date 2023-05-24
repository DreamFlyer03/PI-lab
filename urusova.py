import streamlit as st


def urusova_code():
    st.title("Пассажиры Титаника")
    choise = st.radio('Выберите пол пассажира', ['муж', 'жен'])
    var = st.selectbox('Выберите класс пассажира', ['1', '2', '3'])
    if choise == 'муж':
        choise = 'male'
    else:
        choise = 'female'
    with open("data.csv") as file:
        s = 0
        for line in file:
            lst = line.rstrip().split(',')
            name = lst[3] + lst[4]
            save = lst[1]
            sex = lst[5]
            pclass = lst[2]
            age = lst[6]
            if save == "1" and pclass == var and sex == choise:
                s = s + 1
                st.text(f'Данные пассажира {s}: {name[1:-1]}, {sex}, {age}')
