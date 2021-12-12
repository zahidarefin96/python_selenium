import pytest


@pytest.mark.usefixtures("test_setup")
class TestXExample:

    def test_setupdemo(self):
        print("I will be execute in setup-demo method")

    def test_setupdemo1(self):
        print("I will be execute in setup-demo 1 method")

    def test_setupdemo2(self):
        print("I will be execute in setup-demo 2 method")

    def test_setupdemo3(self):
        print("I will be execute in setup-demo 3 method")
