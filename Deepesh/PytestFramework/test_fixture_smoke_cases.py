import pytest

ENV = "PROD"
"""
fixture is pre-requisite function that we want to execute and before and after test execution.
# fixture scope
1. function
2. class
3. module
4. package
5. session
"""


@pytest.fixture(scope="function", autouse=True)
def setup_fun():
    print("\n----fun execution started----")
    yield
    print("\n----fun execution completed----")


@pytest.fixture(scope="class", autouse=True)
def setup_class():
    print("\n----class execution started----")
    yield
    print("\n----class execution completed----")


@pytest.fixture(scope="module", autouse=True)
def setup_module():
    print("\n----module execution started----")
    yield
    print("\n----module execution completed----")


@pytest.fixture(scope="package", autouse=True)
def setup_package():
    print("\n----package execution started----")
    yield
    print("\n----package execution completed----")


@pytest.fixture(scope="session", autouse=True)
def setup_session():
    print("\n----session execution started----")
    yield
    print("\n----session execution completed----")


class TestSmoke:

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
