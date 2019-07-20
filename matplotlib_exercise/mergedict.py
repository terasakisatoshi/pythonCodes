from collections import ChainMap
def main():
    d1=dict(x=1,y=2,z=3)
    d2=dict(p=1,q=2,r=3)

    merged=ChainMap(*[d1,d2])
    print(merged['x'])
    hoge=dict(**merged)
    print(hoge)

if __name__ == '__main__':
    main()