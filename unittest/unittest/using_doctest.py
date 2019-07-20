"""
doctest を用いた単体テストを試すコードです．
単体テストを実行したい関数に説明を記述する docstring にプログラマーが期待する入力コードを実行します．
そのあと
import doctest
doctest.testmod()
を実行してください
"""

def add(x,y):
    """
    >>> add(3,4)==7
    True
    >>> add(3,4)==8
    True
    """
    return x+y
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()