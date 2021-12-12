# any pytest_learning file should be start with test_ or end with _test
# pytest_learning method names should start with test
# any code should be in method only
# method name should have sense
# -k stands for method name execution; -s stands for logs in output; -v stands for more info like metadata
# we can run specific file with py.test <filename>
# we can mark (tag) tests @pytest.mark.smoke and then run with -m
# we can skip test with @pytest.mark.skip
# no result --> @pytest.mark.xfail
# fixtures are used for setup and tear down methods for test cases- conftest file to generalize
# fixture make it available to all test cases
# data driven parameterization can be done with return statements in tuple format
# when you define fixture scope to class only, it will run once before class is initiated and at the end

import pytest


@pytest.mark.smoke
def test_hello(test_setup):
    print("Hello")


def test_greet():
    print("Good morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
