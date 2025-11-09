import pytest

@pytest.mark.smoke
def test_addition():
    n1 = 50
    n2 = 60
    assert n1 + n2 == 110

@pytest.mark.smoke
def test_multiplication():
    v1 = 5
    v2 = 6
    assert v1*v2 == 30

@pytest.mark.smoke
def test_division():
    n1 = 50
    n2 = 5
    assert n1//n2 == 10

@pytest.mark.regression
def test_subtraction():
    b1= 500
    b2 = 50
    assert b1 - b2 == 400

