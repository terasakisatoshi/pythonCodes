# coding utf-8
import pprint
import requests

"""
If one use this script with python3,
you must install 'requests' package in advance.
$ pip install requests
"""

def main():
    user='terasakisatoshi'
    response=requests.get('https://api.github.com/users/%s/repos' % user)
    #for repo in response.json():
    #    pprint.pprint(repo)

    #get example
    pprint.pprint(response.json()[len(response.json())//2])

if __name__ == '__main__':
    main()