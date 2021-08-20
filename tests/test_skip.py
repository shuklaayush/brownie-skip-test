import pytest


@pytest.mark.skip()
def test_skip():
    assert True

def test_noskip():
    assert True