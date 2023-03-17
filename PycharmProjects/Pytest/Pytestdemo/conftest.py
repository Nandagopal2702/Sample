import pytest


@pytest.fixture(scope="class")
def setup():
    print("i will be executing first")
    yield
    print("i will be executing last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Nandu", "Gopal", "Nandagopal"]


@pytest.fixture(params=[("Chrome", "Nandu", "gopal"), ("Firefox", "Nandu"), "IE"])
def crossBrowser(request):
    return request.param
