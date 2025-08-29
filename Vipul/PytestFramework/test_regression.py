import pytest

ENV = "prod"

@pytest.mark.regression
def test_add():
    a = 10
    b = 20
    print("addition is :", a+b)
    assert a + b == 30

@pytest.mark.smoke
def test_sub():
    a = 10
    b = 20
    print("addition is :", a-b)
    assert a - b == -10

@pytest.mark.smoke
def test_mul():
    a = 10
    b = 20
    print("addition is :", a*b)
    assert a * b == 200

@pytest.mark.skipif(ENV == "stage", reason = "this functionality is not available on QA environment")
def test_div():
    a = 100
    b = 20
    print("addition is :", a/b)
    assert a / b == 5