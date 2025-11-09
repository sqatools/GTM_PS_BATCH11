import pytest

@pytest.mark.skip
def test_login():
    print("Login done")

@pytest.mark.regression
def test_addProduct():
    print("add product")