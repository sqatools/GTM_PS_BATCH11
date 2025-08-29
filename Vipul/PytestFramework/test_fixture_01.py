import pytest

# @pytest.mark.usefixtures("setup")
class Test_fixture_01:

    def test_add(self):
        a = 10
        b = 20
        print("addition result is ::", a+b)

    def test_sub(self):
        a = 10
        b = 20
        print("subtraction result is ::", a-b)

