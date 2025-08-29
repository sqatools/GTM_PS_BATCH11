import pytest


@pytest.mark.smoke
def test_addition():
    n1 = 40
    n2 = 30
    assert n1 + n2 == 70


@pytest.mark.smoke
def test_multiplication():
    a1 = 5
    a2 = 8
    assert a1*a2 == 40


@pytest.mark.smoke
def test_division():
    b1 = 40
    b2 = 10
    assert b1//b2 == 4


@pytest.mark.smoke
def test_subtraction():
    c1 = 300
    c2 = 100
    assert c1 - c2 == 300

@pytest.mark.sanity
@pytest.mark.smoke
def test_addition1():
    n1 = 40
    n2 = 30
    assert n1 + n2 == 70


@pytest.mark.sanity
def test_multiplication1():
    a1 = 5
    a2 = 8
    assert a1*a2 == 40


@pytest.mark.sanity
def test_division1():
    b1 = 40
    b2 = 10
    assert b1//b2 == 4


@pytest.mark.sanity
def test_subtraction1():
    c1 = 300
    c2 = 100
    assert c1 - c2 == 300


@pytest.mark.regression
def test_addition2():
    n1 = 40
    n2 = 30
    assert n1 + n2 == 70


@pytest.mark.regression
def test_multiplication2():
    a1 = 5
    a2 = 8
    assert a1*a2 == 40


@pytest.mark.regression
def test_division2():
    b1 = 40
    b2 = 10
    assert b1//b2 == 4


@pytest.mark.regression
def test_subtraction2():
    c1 = 300
    c2 = 100
    assert c1 - c2 == 300