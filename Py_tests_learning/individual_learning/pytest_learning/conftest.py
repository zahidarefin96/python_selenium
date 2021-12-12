import pytest


@pytest.fixture(scope="class")
def test_setup():
    print("I will be executed first")
    yield
    print("I will be executed last")


@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Md", "Arefin", "rahulshettyacademy.com"]


@pytest.fixture(params=[("chrome", "Md", "Arefin"), ("Firfox", "Zahid"), ("IE", "Safari")])
def crossBrowser(request):
    return request.param
