from urllib import request

url="http://www.google.com"

conn = request.urlopen(url)
print(conn.getheader('Content-Type'))
for key, value in conn.getheaders():
    print(key,"=", value)
print(conn.status)
#print(conn.read())