"""
pytest will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories. More generally, it follows standard test discovery rules.
"""

import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    """
    Use the raises helper to assert that
    some code raises an exception.
    """
    with pytest.raises(SystemExit):
        f()
