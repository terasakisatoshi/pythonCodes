"""
unit test using unittest

classを定義するときに
unittest.TestCase
を継承する．

unittest.TestCaseのサブクラスとすることで自動的に unittest の
テストケースであると認識される。

単体テストを実行したい関数をクラスメソッドとして定義する．
関数名は必ず test を頭につけることにする．
"""

import unittest

def add(x,y):
    return x+y

class unitTest(unittest.TestCase):
    """
    for unittest
    """

    def setUp(self):
        """"
        テストするときに呼び出されるもの
        """
        self.a=3
        self.b=4

    def tearDown(self):
        """
        テスト対象が終了したときに実行される
        """
        print("done unit test")

    def test_add(self):
        self.assertEqual(add(self.a,self.b),7)

    def test_fake_add(self):
        self.assertEqual(add(self.a,self.b),8)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
