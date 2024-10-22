import pytest


# @pytest.fixture()
# def setup():
#     print("I will be exucute first")
#     yield
#     print("I will be executed last")
@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixturedemo(self):
        print("I will execute steps in fixture methods")

    def test_fixturedemo1(self):
        print("I will execute steps in fixture methods")

    def test_fixturedemo2(self):
        print("I will execute steps in fixture methods")

    def test_fixturedemo3(self):
        print("I will execute steps in fixture methods")