#! /usr/local/bin/python3
from client import Client
from settings import *


class Printer(Client):
    client_type = 'printer'


def main():
    printer = Printer(SERVER_HOST, SERVER_PORT)
    while True:
        msg = printer.get_message()
        print('Print message: %s' % msg)
        printer.send_message({'status': 'OK'})


if __name__ == '__main__':
    main()
