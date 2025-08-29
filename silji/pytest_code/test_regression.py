import pytest
@pytest.mark.regression
@pytest.mark.smoke
def test_addition():
    n1 = 50
    n2 = 60
    assert n1 + n2 == 110

@pytest.mark.regression
def test_multiplication2():
    v1 = 5
    v2 = 6
    assert v1*v2 == 30

@pytest.mark.skip
def test_division3():
    n1 = 50
    n2 = 5
    assert n1//n2 == 10

@pytest.mark.smoke
def test_subtraction4():
    b1= 500
    b2 = 50
    assert b1 - b2 == 450

