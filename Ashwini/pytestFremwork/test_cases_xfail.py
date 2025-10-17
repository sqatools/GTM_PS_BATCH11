import pytest


def test_addition():
    n1=20
    n2=20
    assert n1+n2==40
@pytest.mark.xfail
def test_subtraction():
    v1=300
    v2=10
    assert v1-v2== 200


def test_multiplication():
    p1=5
    p2=6
    assert p1*p2==30

@pytest.mark.xfail
def test_division():
    v1=500
    v2=10
    assert v1//v2==50
