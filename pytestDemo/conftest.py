import pytest


@pytest.fixture(scope="class")     #this fixture will only work on class, as scope mentioned class
def setup():
    print("I will be exucute first")
    yield
    print("I will be executed last")

@pytest.fixture()      #data driven fixture
def dataLoad():
    print("user profile data is being created")
    return ["Rahul","Shetty","rahulshettyacademy.com"]

@pytest.fixture(params=[("chrome","Rahul"),("Firefox","Shetty"),"IE"])      #parameterize fixture
def crossBrowser(request):
    return request.param
