from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsoup = BeautifulSoup(html.read())
        title = bsoup.body.h1
    except AttributeError as e:
        return None
    return title


def main():
    URL="http://www.pythonscraping.com/pages/page1.html"
    title=get_title(URL)
    if title==None:
        print("Title could not be found")
    else:
        print(title)


if __name__ == '__main__':
    main()
