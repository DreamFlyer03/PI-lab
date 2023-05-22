import streamlit as st


def get_pass_list(data, sex, pclass):
    if sex == 'муж':
        sex = 'male'
    else:
        sex = 'female'
    out_list = []
    for line in data:
        lst = line.rstrip().split(",")
        if lst[1] == "1" and lst[2] == pclass and lst[5] == sex:
            out_list += [lst[3]+''+lst[4]+', '+lst[5]+', '+lst[6]]
    return out_list


def urusova_code():
    with open("data.csv") as file:
        data = file.readlines()
    sex = st.radio('Выберите пол пассажира:', ['муж', 'жен'])
    pclass = st.selectbox('Выберите класс полета:', ['1', '2', '3'])
    st.table({"Спасенные пассажиры (имя, пол,возраст):": get_pass_list(data, sex, pclass)})


urusova_code()
