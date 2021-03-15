import pytest


@pytest.fixture()
def setup():
    print('exec setup')


# adding setup means, it will call setup for this test.
def test1(setup):
    print('exec test1')
    assert 2 == 3


@pytest.mark.usefixtures("setup")
def test2():
    print('exec test2')
    assert 1 == 1
