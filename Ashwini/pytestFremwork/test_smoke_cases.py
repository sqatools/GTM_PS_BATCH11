import pytest

import pytest
ENV = "TEST"

@pytest.mark.smoke
def test_addition():
    num=20
    num1=30
    assert num+num1==50

@pytest.mark.smoke
def test_subtraction():
    n1=30
    n2=10
    assert n1-n2==20

@pytest.mark.skip
@pytest.mark.smoke
def test_multiplication():
    v1=5
    v2=4
    assert v1*v2==20
@pytest.mark.skip( ENV == "TEST",reason="This code is not available in test ENV")
@pytest.mark.sanity
def test_division():
    n1=50
    n2=5
    assert n1//n2==10

@pytest.mark.regression
def test_addition1():
    num=20
    num1=30
    assert num+num1==50
@pytest.mark.sanity
def test_subtraction2():
    n1=30
    n2=10
    assert n1-n2==10
@pytest.mark.smoke
def test_multiplication3():
    v1=5
    v2=4
    assert v1*v2==20
@pytest.mark.regression
def test_division4():
    n1=50
    n2=5
    assert n1//n2==10

@pytest.mark.smoke
@pytest.mark.sanity
def test_addition5():
    num=20
    num1=30
    assert num+num1==50
@pytest.mark.regression
def test_subtraction6():
    n1=30
    n2=10
    assert n1-n2==10

@pytest.mark.smoke
@pytest.mark.sanity
def test_multiplication7():
    v1=5
    v2=4
    assert v1*v2==20


@pytest.mark.regression
def test_division8():
    n1=50
    n2=5
    assert n1//n2==10
