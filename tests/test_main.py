''' My Calculator Test'''
from app.main import addition

def test_addition():
    '''Addition funtion'''
    assert addition(1,1)  == 2
