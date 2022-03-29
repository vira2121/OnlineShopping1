import pytest

@pytest.fixture(scope="session",autouse=True)
def setUp():
    print("Open Amazon app")
    print("User logged in")
    yield
    print("User logged out")
    print("Close Amazon app")