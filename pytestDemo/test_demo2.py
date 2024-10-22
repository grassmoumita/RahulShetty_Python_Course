import pytest


@pytest.mark.smoke
@pytest.mark.skip     #to skip a test case
def test_firstProgram():
    msg = "Good Morning"
    assert msg == "Good Morning"


def test_secondCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"


