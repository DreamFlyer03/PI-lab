from Starkovskaya import count_depending_sex_and_save
import pandas as pd


def test_do_dataframe_if_save_for_survived_male():
    grid = {'Survived': [0, 0, 1, 0, 1],
            'Sex': ['male', 'female', 'male', 'female', 'female'],
            'Name': ['PassengerOne', 'PassengerTwo', 'PassengerTree', 'PassengerFour', 'PassengerFive'],
            'Age': [22, 0, 18, 18, 14],
            'Pclass': [1, 2, 3, 1, 2]}

    test_data = pd.DataFrame(grid)
    left = count_depending_sex_and_save(test_data, "male", 1)
    right = pd.DataFrame({'Name': ['PassengerTree'], 'Age': [18], 'Pclass': [3]})
    pd.testing.assert_frame_equal(left.reset_index(drop=True), right.reset_index(drop=True))


def test_do_dataframe_if_save_for_survived_female():
    grid = {'Survived': [0, 0, 1, 0, 1],
            'Sex': ['male', 'female', 'male', 'female', 'female'],
            'Name': ['PassengerOne', 'PassengerTwo', 'PassengerTree', 'PassengerFour', 'PassengerFive'],
            'Age': [22, 0, 18, 18, 14],
            'Pclass': [1, 2, 3, 1, 2]}

    test_data = pd.DataFrame(grid)
    left = count_depending_sex_and_save(test_data, "female", 1)
    right = pd.DataFrame({'Name': ['PassengerFive'], 'Age': [14], 'Pclass': [2]})
    pd.testing.assert_frame_equal(left.reset_index(drop=True), right.reset_index(drop=True))


def test_do_dataframe_if_save_if_empty_fields():
    grid = {'Survived': [0, 0, 1, 0, 1],
            'Sex': ['male', 'female', 'male', None, 'female'],
            'Name': ['PassengerOne', 'PassengerTwo', 'PassengerTree', 'PassengerFour', None],
            'Age': [22, 0, 10, 18, 14],
            'Pclass': [1, 2, 3, 1, 2]}

    test_data = pd.DataFrame(grid)
    left = count_depending_sex_and_save(test_data, "female", 1)
    right = pd.DataFrame({'Name': None, 'Age': [14], 'Pclass': [2]})
    pd.testing.assert_frame_equal(left.reset_index(drop=True), right.reset_index(drop=True))
