from Sarkisov import price


# проверка подсчётов по тестовому набору данных
# проверка значения средней стоимости билета для мужчин. В тестовом наборе он равен 7.25
def test_midl_price_male():
    test_data = '''PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
1,0,3,"Mister X",male,22,1,0,A1 21171,7.25,,S
2,1,1,"Miss X",female,38,1,0,PC 17599,71.2833,C85,C
3,1,3,"Miss Y",female,26,0,0,STON/O2. 3101282,7.925,C61,S
'''
    result = price(test_data)
    assert result[0] == 7.25

    
# проверка подсчётов по тестовому набору данных
# проверка значения средней стоимости билета для женщин. В тестовом наборе он равен 50 (100 + 30 ) / 2
def test_midl_price_female():
    test_data = '''PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
1,0,3,"Mister X",male,22,1,0,A1 21171,7.25,,S
2,1,1,"Miss X",female,38,1,0,PC 17599,70,C85,C
3,1,3,"Miss Y",female,26,0,0,STON/O2. 3101282,30,C61,S
'''
    result = price(test_data)
    assert result[1] == 50
