from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler

ip = '127.0.0.1'
port = 8000
print('port={}'.format(port))
handler = SimpleHTTPRequestHandler
server = HTTPServer((ip, port), handler)

server.serve_forever()
