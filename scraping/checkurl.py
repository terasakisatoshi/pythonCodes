from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen("https://pythonscrapingthisurldoesnotexist.com")
except HTTPError as e:
    print("execpt HTTPError")
    print(e)
except URLError as e:
    print("URLError")
    print(e)
else:
    print("It worked")