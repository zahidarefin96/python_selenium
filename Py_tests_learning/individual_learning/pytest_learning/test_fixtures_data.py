import pytest

from individual_learning.pytest_learning.base_class import base_class


@pytest.mark.usefixtures("dataLoad")
class TestExample2(base_class):

    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        log.info("dataLoad[0])")
        log.info("dataLoad[2]")
        print(dataLoad[2])
