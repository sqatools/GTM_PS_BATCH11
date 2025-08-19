import pytest

ENV = "PROD"

@pytest.mark.usefixtures("class_fixture")
class TestSmokeClass:

    @pytest.mark.smoke
    def test_addition(self):
        n1 = 50
        n2 = 60
        assert n1 + n2 == 110

    @pytest.mark.skip
    @pytest.mark.smoke
    def test_multiplication(self, ):
        v1 = 5
        v2 = 6
        assert v1 * v2 == 30

    @pytest.mark.skipif(ENV == "TEST", reason="This code is not available in test ENV")
    @pytest.mark.smoke
    def test_division(self):
        n1 = 50
        n2 = 5
        assert n1 // n2 == 10

    def test_subtraction(self):
        b1 = 500
        b2 = 50
        assert b1 - b2 == 400

    @pytest.mark.smoke
    def test_addition1(self):
        n1 = 50
        n2 = 60
        assert n1 + n2 == 110

    @pytest.mark.sanity
    def test_multiplication2(self):
        v1 = 5
        v2 = 6
        assert v1 * v2 == 30

    @pytest.mark.smoke
    @pytest.mark.sanity
    def test_division3(self):
        n1 = 50
        n2 = 5
        assert n1 // n2 == 10
