import pytest

from Pytestdemo.Baseclass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample(BaseClass):
    def test_editProfile(self, dataLoad):
        log = self.getlogger()
        log.info(dataLoad[0])
        log.info(dataLoad[2])
        print(dataLoad[2])
