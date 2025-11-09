import pytest

ENV = "PROD"

class TestSmoke:

    @pytest.mark.smoke
    def test_addition(self):
        n1 = 50
        n2 = 60
        assert n1 + n2 == 110

    def test_multiplication(self):
        v1 = 5
        v2 = 6
        assert v1 * v2 == 30

    @pytest.mark.skip
    @pytest.mark.smoke
    def test_division(self):
        n1 = 50
        n2 = 5
        assert n1 // n2 == 10

    @pytest.mark.regression
    def test_subtraction(self):
        b1 = 500
        b2 = 50
        assert b1 - b2 == 400