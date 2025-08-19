
import pytest

ENV = "PROD"

@pytest.mark.smoke
def test_addition():
    n1 = 10
    n2 = 60
    assert n1 + n2 == 70


# @pytest.mark.skip
@pytest.mark.smoke
def test_multiplication():
    v1 = 15
    v2 = 6
    assert v1*v2 == 90


@pytest.mark.skipif(ENV == "TEST", reason="This code is not available in test ENV")
@pytest.mark.smoke
def test_division():
    n1 = 100
    n2 = 5
    assert n1//n2 == 20


def test_subtraction():
    b1= 500
    b2 = 50
    assert b1 - b2 == 450


@pytest.mark.smoke
def test_addition1():
    n1 = 50
    n2 = 60
    assert n1 + n2 == 110


@pytest.mark.sanity
def test_multiplication2():
    v1 = 5
    v2 = 6
    assert v1*v2 == 30

@pytest.mark.smoke
@pytest.mark.sanity
def test_division3():
    n1 = 50
    n2 = 5
    assert n1//n2 == 10

@pytest.mark.sanity
def test_subtraction4():
    b1= 500
    b2 = 50
    assert b1 - b2 == 400

@pytest.mark.sanity
def test_addition5():
    n1 = 50
    n2 = 60
    assert n1 + n2 == 110

@pytest.mark.smoke
@pytest.mark.regression
def test_multiplication6():
    v1 = 5
    v2 = 6
    assert v1*v2 == 30

@pytest.mark.regression
def test_division7():
    n1 = 50
    n2 = 5
    assert n1//n2 == 10

@pytest.mark.regression
def test_subtraction8():
    b1= 500
    b2 = 50
    assert b1 - b2 == 400



