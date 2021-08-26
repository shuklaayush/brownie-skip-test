import pytest

@pytest.mark.skip(reason="No reason")
def test_skip():
    pytest.fail('hello')
    assert True

@pytest.mark.require_network("dummy")
def test_mark():
    pass

def test_noskip():
    assert True