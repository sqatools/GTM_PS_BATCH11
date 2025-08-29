import pytest

ENV = "PROD"

@pytest.mark.smoke
@pytest.mark.skip
def test_addition():
    n1 = 100
    n2 = 100
    assert n1 + n2 == 200

@pytest.mark.sanity
@pytest.mark.skipif(ENV == "TEST", reason="This code is not available in test ENV")

def test_multiplication():
    v1 = 5
    v2 = 5
    assert v1*v2 == 25