class お布団(object):

    def __init__(self):
        print("眠いよ")

    def __enter__(self):
        print("入眠")
        return self

    def __exit__(self, type_, value, traceback):
        print(type_, value, traceback)
        print("起床")
        return True

    def 状態確認(self):
        print("オフトニアなうZzz")


def main():
    with お布団() as 布団:
        # 布団.起きたいか()
        布団.状態確認()

if __name__ == '__main__':
    main()
