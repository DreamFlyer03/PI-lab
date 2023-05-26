from MakarNV import get_pass_list


def test_pass_list_male():
    data = ['0,1,2,3,4,female', '0,1,2,3,4,male', '0,1,2,3,4,female']
    assert get_pass_list(data, 'мужчины', '1') == ['0,1,2,3,4,male']


def test_pass_list_female():
    data = ['0,1,2,3,4,male'', '0,1,2,3,4,female', '0,1,2,3,4,male']
    assert get_pass_list(data, 'женщины', '1') == ['0,1,2,3,4,female']



