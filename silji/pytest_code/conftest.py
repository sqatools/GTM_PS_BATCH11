import pytest

@pytest.fixture(scope="class")
def class_fixture():
    print("----- Welcome to class test execution------")
    yield
    print("----- class test execution completed------")

