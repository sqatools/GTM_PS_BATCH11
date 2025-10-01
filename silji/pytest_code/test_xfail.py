import pytest

@pytest.mark.xfail
def test_division():
    n1 = 50
    n2 = 5
    assert n1//n2 == 10

@pytest.mark.xfail
def test_subtraction():
    b1= 500
    b2 = 50
    assert b1 - b2 == 450

def test_addition1():
    n1 = 50
    n2 = 60
    assert n1 + n2 == 110