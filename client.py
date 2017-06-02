# -*- coding: utf8 -*-
from socket import socket, AF_INET, SOCK_STREAM
from settings import *
import json


class Client(object):
    client_type = 'client'

    def __init__(self, host, port):
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.connect((host, port))

        self.send_message({'client_type': self.client_type})

    def send_message(self, msg):
        self.sock.sendall(bytes(json.dumps(msg), 'utf8'))

    def get_message(self):
        raw = self.sock.recv(BUFFER_SIZE)
        print(raw)
        return json.loads(str(raw, 'utf8'))
