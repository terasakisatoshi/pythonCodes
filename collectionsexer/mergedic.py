from collections import ChainMap


def main():
    d1 = {"A": 1, "B": 2}
    d2 = {"C": 3, "D": 4}
    d3 = {"A": 5, "B": 6}
    connected = dict(ChainMap(d1, d2))
    print(connected)
    connected = dict(ChainMap(d3, connected))
    print(connected)
    
if __name__ == '__main__':
    main()
