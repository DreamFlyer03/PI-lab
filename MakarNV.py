import streamlit as st

def V2_MakarNV():
        st.title('Пассажиры Титаника')
        st.header("""Определим, кто из пассажиров выжил, а кто – нет.""")
        var = st.selectbox("Спасены?", ['да' , 'нет'])
        choise = st.radio('Выбрать пол пассажира:', ["женский", "мужской"])
        if choise == 'мужской':
                choise = 'male'
        else:
                choise = 'female'

        with open("data.csv") as titanic_data:
                s = 0
                for line in titanic_data:
                        lst = line.rstrip().split(',')
                        pclass = lst[2]
                        if pclass == 'Pclass':
                                continue
                        name = lst[3] + lst[4]
                        age = lst[6]
                        sex = lst[5]
                        save = lst[1]
                        if save == "1" and sex == choise:
                                st.text(f'Данные о пассажирах: {pclass}, {name[1:-1]}, {sex}, {age}')