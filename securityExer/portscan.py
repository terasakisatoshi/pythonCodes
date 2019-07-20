import argparse
import socket


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', type=str, help='target address', default='127.0.0.1')
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    ports = range(7000, 9000)
    openports = []
    for port in ports:
        sock = socket.socket()
        print('check port={}'.format(port))
        ret = sock.connect_ex((args.ip, port))
        if ret == 0:
            print('open')
            openports.append(port)
    print(openports)
if __name__ == '__main__':
    main()
