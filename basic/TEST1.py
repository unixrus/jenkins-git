import pytest


@pytest.fixture(autouse=True)
def setup():
    print('exec setup')


def test3():
    print('exec test3')
    assert True


def test4():
    print('exec test4')
    assert True
