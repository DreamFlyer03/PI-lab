# Основной файл проекта командной работы, команда №2 группа ПИ-4см
# Состав команды:
# Сустретов Иван Сергеевич - руководитель проекта
# Суханова Наталия Александровна
# Старковская Татьяна Валентиновна
# Урусова Ольга Александровна
# Макар Надежда Владимировна
# Липанин Вадим Александрович
# Саркисов Андрей Юрьевич

import streamlit as st
# подключаем модули коллег-коллабораторов
import Starkovskaya as stv
import sukhanova as sna
import Sarkisov as sau
import MakarNV as mnv
import urusova6 as uoa
import sustretov as sis
import stub  # файл-заглушка для отсутствующих работ

st.title("Группа ПИ-4см, команда №2. Совместная работа")
st.header("Титаник продолжает мучительно тонуть")
students = {1: "Сустретов И.С.",
            2: "Суханова Н.А",
            3: "Старковская Т.В.",
            4: "Урусова О.А.",
            5: "Макар Н.В.",
            6: "Липанин В.А.",
            7: "Саркисов А.Ю."}

result = st.radio('Выберите, чью работу требуется запустить:', options=(1, 2, 3, 4, 5, 6, 7),
                  format_func=lambda s: students.get(s))

if result == 6:
    stub.stub_page()  # Используем заглушку для не присланных пока в проект работ
elif result == 1:
    sis.sustretov_code()
elif result == 2:
    sna.sukhanova_code()
elif result == 3:
    stv.starkovskaya_code()
elif result == 4:
    uoa.urusova_code()
elif result == 5:
    mnv.V2_MakarNV()
elif result == 7:
    sau.sarkisov_cod()
