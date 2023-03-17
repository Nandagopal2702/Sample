# file name should start with test_ at the start or _test at the end
# pytest method should start with test
# any code should be wrapped in method only
import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello")

@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Goodmorning")


def test_crossbrowser(crossBrowser):
    print(crossBrowser[0])
    print(crossBrowser[1])