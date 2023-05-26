import numpy as np
from sukhanova import get_input_data_as_pd, filter_pd_data, filter_pd_data_as_list

# первый тест.
# проверка средней стоимости билета (поле Fare) в отфильтрованном наборе данных (фильтр по цене билета, более 270)
# средняя цена билета в такой выборе будет 512.3292


def test_filter_pd_data_avg_fare():
    test_price = 270.0

    csv = get_input_data_as_pd()
    result = filter_pd_data(csv, price=test_price)

    assert np.average(result['Fare'].values) == 512.3292


# второй тест.
# проверка длины отфильтрованного набора данных. Фильтр по цене (поле Fare = 10.0), длина списка должна быть равна 555
def test_filter_data_length():
    test_price = 10.0

    csv = get_input_data_as_pd()
    result = filter_pd_data_as_list(csv, price=test_price)

    assert len(result) == 555
