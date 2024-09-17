''' My Calculator Test'''
from app.main import addition, subtraction

def test_addition():
    '''Addition funtion'''
    assert addition(1,1)  == 2

def test_subtraction():
    '''Addition funtion'''
    assert subtraction(1,1)  == 0
