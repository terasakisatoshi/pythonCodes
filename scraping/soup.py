from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("http://www.pythonscraping.com/pages/page1.html")
bsObj=BeautifulSoup(html.read(),"html5lib")
#extract html
print('\n------------\n',
    bsObj.html,
    '\n------------\n')

print('\n------------\n',
    bsObj.html.body,
    '\n------------\n')
