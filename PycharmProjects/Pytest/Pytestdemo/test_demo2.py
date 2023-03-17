# file name should start with test_ at the start or _test at the end
# pytest method should start with test
# any code should be wrapped in method only
import pytest



@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings does not Match"



def test_SecondCreditCard():
    a = 2
    b = 6
    assert a+4 == 6