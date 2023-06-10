import pandas as pd
from lipanin import get_pass_list


def test_get_pass_list_male_survivors():
    grid = {'Survived': [0, 0, 1, 0, 1],
            'Sex': ['male', 'female', 'male', 'female', 'female'],
            'Name': ['PassengerOne', 'PassengerTwo', 'PassengerTree', 'PassengerFour', 'PassengerFive'],
            'Age': [22, 0, 18, 18, 14],
            'Pclass': [1, 2, 3, 1, 2]}

    test_data = pd.DataFrame(grid)
    left = get_pass_list(test_data, "мужской", 0, 100)
    right = ["PassengerTree, male, 18 лет"]
    assert left == right


def test_get_pass_list_female_survivors():
    grid = {'Survived': [0, 0, 1, 0, 1],
            'Sex': ['male', 'female', 'male', 'female', 'female'],
            'Name': ['PassengerOne', 'PassengerTwo', 'PassengerTree', 'PassengerFour', 'PassengerFive'],
            'Age': [22, 0, 18, 18, 14],
            'Pclass': [1, 2, 3, 1, 2]}

    test_data = pd.DataFrame(grid)
    left = get_pass_list(test_data, "женский", 0, 100)
    right = ["PassengerFive, female, 14 лет"]
    assert left == right
