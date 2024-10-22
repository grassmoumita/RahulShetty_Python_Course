#any pytest file with start with test_
#pytest method should start with test
#method name is test case name
#py.test --html=report.html -s    to run html report


import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")

@pytest.mark.xfail       #this test case will run, but won't be print
def test_secondGreatCreditCard():
    print("Good Morning")

def test_crossBrowser(crossBrowser):
    # print(crossBrowser)
    print(crossBrowser[1])



