"""
Test the task data type
"""

from collections import namedtuple

import pytest

Task = namedtuple("Task", ["summary", "owner", "done", "id"])
Task.__new__.__defaults__ = (None, None, False, None)


def test_defaults():
    """Using no parameters should invoke defaults."""
    task1 = Task()
    task2 = Task(None, None, False, None)
    assert task1 == task2

@pytest.mark.run_these_please
def test_member_access():
    """Chech .field functionality of namedtuple."""
    t = Task("buy milk", "Brian")
    assert t.summary == "buy milk"
    assert t.owner == "Brian"
    assert (t.done, t.id) == (False, None)


def test_asdict():
    """_asdict() should return a dictionary"""
    t_task = Task("do something", "Okken", True, 21)
    t_dict = t_task._asdict()
    expected = {
        "summary": "do something",
        "owner": "Okken",
        "done": True,
        "id": 21
    }
    assert t_dict == expected

def task_replace():
    """_replace() should change passed in fields"""
    t_before = Task("finish book", "brian", False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task("finish book", "brian", True, 10)
    assert t_after == t_expected
    

def main():
    t = Task("Buy milk", "Brian")
    print(t)
    t_dict = t._asdict()
    print(t_dict)


if __name__ == '__main__':
    main()
