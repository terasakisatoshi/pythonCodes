class Background():
    W = "this is background"


class MainClass():

    def __init__(self):
        self._bg = Background()

    @property
    def W(self):
        return self._bg.W

    @W.setter
    def W(self, weight):
        self._bg.W = weight


def main():
    klass = MainClass()
    print(klass.W)
    klass.W = "updated background's property named W"
    print(klass.W)
if __name__ == '__main__':
    main()
