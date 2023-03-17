import pytest


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureDemo(self):
        print("i will be executing the fixture demo program")

    def test_fixtureDemo1(self):
        print("i will be executing the fixture demo1 program")

    def test_fixtureDemo2(self):
        print("i will be executing the fixture demo2 program")

    def test_fixtureDemo3(self):
        print("i will be executing the fixture demo3 program")