from pprint import pprint
import requests

BASE = 'https://ethermine.org/api/miner_new'
WALLET = 'e4835acb3fbbcd45b3f448ea5168292435afdc49'


def main():
    try:
        res = requests.get('%s/%s' % (BASE, WALLET))
    except Exception as e:
        print(e)
        print('maybe you request too many ... try again later')
    #parse response 'res' as 'dict' object
    res=res.json()
    print('total hash=', res['reportedHashRate'])
    for worker,info in res['workers'].items():
        print('worker=',worker)
        print(info['hashrate'])


if __name__ == '__main__':
    main()
