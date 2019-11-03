"""
Once you develop multiple tests,
you may want to group them into a class.
`pytest` makes it easy to create a class containing more than one test:
"""

# content of test_class.py


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
