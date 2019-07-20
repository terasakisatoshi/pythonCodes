from __future__ import print_function
import socket
from contextlib import closing

def main():
  host = '127.0.0.1'
  port = 4000
  backlog = 10
  bufsize = 4096

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  with closing(sock):
    sock.bind((host, port))
    sock.listen(backlog)
    while True:
      conn, address = sock.accept()
      with closing(conn):
        print("address",address)
        msg = conn.recv(bufsize)
        print(msg)
        msg+="from serever"
        conn.send(msg)
  return

if __name__ == '__main__':
  main()