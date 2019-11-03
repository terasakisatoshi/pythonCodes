"""
pytest allows you to use the standard python assert for verifying expectations and values in Python tests. For example, you can write the folowing:
"""


def f():
    return 3


def test_function():
    assert f() == 4
