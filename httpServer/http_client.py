import requests


def access_google():
    url = 'http://www.google.com/'
    res = requests.get(url)
    if res.status_code == 200:
        for k, v in dict(res.headers).items():
            print('key: {}, value: {}'.format(k, v))
    print('res.text=')
    print(res.text)


def access_local(port):
    url = 'http://localhost:{}'.format(port)
    res = requests.get(url)
    if res.status_code == 200:
        for k, v in dict(res.headers).items():
            print('key: {}, value: {}'.format(k, v))
        print('res.text=')
        print(res.text)


def main():
    # access_google()
    access_local(port=8000)

if __name__ == '__main__':
    main()
