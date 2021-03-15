import pytest
from pytest import request


@pytest.fixture()
def setup1():
    print('exec setup1')
    yield
    print('\n teardown 1')


@pytest.fixture()
def setup2():
    print('exec setup2')

    def teardown_a():
        print('\nTeardown A')

    def teardown_b():
        print('\nTeardown B')

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)


def test5(setup1):
    print('exec test5')
    assert False


def test6(setup2):
    print('exec test6')
    assert False

'''
test fixture scope -
Function - Run the fixture once for each test
Class    - Run the fixture once for each class of tests
Module   - Run once when module goes in scope
Session  - The fixture is run when py starts
'''
