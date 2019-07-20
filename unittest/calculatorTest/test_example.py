import unittest


class MyTestClass(unittest.TestCase):

    def test_test1(self):
        print("Hi")

    def test_test2(self):
        print("Hello")

    def func(self):
        """you must set prefix `test`"""
        print("NoCheck")

    def test_assert_true(self):
        self.assertTrue(1 + 2 == 3)

    def test_assert_eq(self):
        self.assertEqual(3, 1 + 2)

    def test_assert_neq(self):
        self.assertNotEqual(-1, 1)

    def test_assert_in(self):
        self.assertIn("a", "abc")


def main():
    unittest.main()

if __name__ == '__main__':
    main()
