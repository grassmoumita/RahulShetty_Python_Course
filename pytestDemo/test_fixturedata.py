import pytest

from pytestDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_editProfile(self, dataLoad):
        log = self.getlogger()
        log.info(dataLoad[1])
        log.info(dataLoad[2])
        # print(dataLoad)
        # print(dataLoad[1])

