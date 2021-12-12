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

import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_hi():
    msg = "Hello"
    assert msg == "Hi", "Test failed, condition did not match"


@pytest.mark.xfail
def test_addition():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition did not match"


