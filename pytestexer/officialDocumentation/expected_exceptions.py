"""
In order to write assertions about raised
exceptions, you can use pytest.raises
as a context manager like this:
"""

import pytest


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1/0
