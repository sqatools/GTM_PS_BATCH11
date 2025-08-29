import pytest

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