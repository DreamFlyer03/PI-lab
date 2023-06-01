import streamlit as st
import csv


def price(csv_file):
    min_price_male = 0
    max_price_male = 0
    midl_price_male = 0
    all_price_male = 0
    min_price_female = 0
    max_price_female = 0
    midl_price_female = 0
    all_price_female = 0
    csv_reader = csv.DictReader(csv_file)
    cont_male = 0
    cont_female = 0
    for row in csv_reader:
        if row["Sex"] == "male":
            cont_male += 1
            all_price_male += float(row["Fare"])
            if float(row["Fare"]) > max_price_male:
                max_price_male = float(row["Fare"])
            if float(row["Fare"]) < min_price_male or min_price_male == 0:
                min_price_male = float(row["Fare"])
            if row["Sex"] == "female":
                cont_female += 1
                all_price_female += float(row["Fare"])
            if float(row["Fare"]) > max_price_female:
                max_price_female = float(row["Fare"])
            if float(row["Fare"]) < min_price_female or min_price_female == 0:
                min_price_female = float(row["Fare"])

    midl_price_male = all_price_male / cont_male
    midl_price_female = all_price_female / cont_female

    return midl_price_male, midl_price_female, min_price_male, max_price_male, min_price_female, max_price_female


def sarkisov_cod():
    st.title("Титаник")
    st.write("---")
    variables = [" ", "Мужчины", "Женщины"]
    default_variable = variables[0]
    with open('data.csv', mode='r') as csv_file:
        midl_price_male, midl_price_female, min_price_male, max_price_male, min_price_female, max_price_female = price(csv_file)
    selected_variable = st.selectbox("Выберите пол:", variables, index=variables.index(default_variable))
    if selected_variable == "Мужчины":
        st.write("Минимальная цена билета для пассажиров мужского пола: {:.2f}".format(min_price_male))
        st.write("Максимальная цена билета для пассажиров мужского пола: {:.2f}".format(max_price_male))
        st.write("Средняя цена  билета для пассажиров мужского пола: {:.2f}".format(midl_price_male))
    elif selected_variable == "Женщины":
        st.write("Минимальная цена билета для пассажиров женского пола: {:.2f}".format(min_price_female))
        st.write("Максимальная цена билета для пассажиров женского пола: {:.2f}".format(max_price_female))
        st.write("Средняя цена билета для пассажиров женского пола: {:.2f}".format(midl_price_female))
            
sarkisov_cod()
