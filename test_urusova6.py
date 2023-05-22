from main import *


def test_pass_list_male():
    data = ['1,1,3,"Braund, Mr. Owen Harris",male,22', '7,1,1,"McCarthy, Mr. Timothy J",male,54',
            '11,1,3,"Sandstrom, Miss. Marguerite Rut",female,42',
            '15,0,3,"Vestrom, Miss. Hulda Amanda Adolfina",female,34']
    assert get_pass_list(data, 'муж', '1') == ['"McCarthy Mr. Timothy J", male, 54']


def test_pass_list_female():
    data = ['1,1,3,"Braund, Mr. Owen Harris",male,22', '7,1,1,"McCarthy, Mr. Timothy J",male,54',
            '11,1,3,"Sandstrom, Miss. Marguerite Rut",female,42',
            '15,0,3,"Vestrom, Miss. Hulda Amanda Adolfina",female,34']
    assert get_pass_list(data, 'жен', '1') == []
