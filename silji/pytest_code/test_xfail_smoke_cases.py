import pytest

ENV = "PROD"


@pytest.mark.xfail
def test_subtraction8():
    b1= 500
    b2 = 50
    assert b1 - b2 == 400
