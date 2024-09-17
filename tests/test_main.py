''' My Calculator Test'''
import pytest
from app.main import addition, division, multiplication, subtraction

def test_addition():
    '''Addition funtion'''
    assert addition(1,1)  == 2

def test_subtraction():
    '''Subtraction funtion'''
    assert subtraction(1,1)  == 0

def test_multiplication():
    '''Subtraction funtion'''
    assert multiplication(2,2)  == 4

def test_division():
    '''Division Function'''
    assert division(2,2) == 1


def test_division_by_zero_exception():
    '''Division Function testing that I get the exception divide by zero'''
    with pytest.raises(ZeroDivisionError):
        division(10,0)
