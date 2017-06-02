#! /usr/local/bin/python3
from queue import Queue
from socketserver import ThreadingMixIn, TCPServer, BaseRequestHandler
from settings import *
import json


class Database():
    def __init__(self):
        self.payments = []

    @property
    def total_money(self):
        if self.payments:
            return sum(p['money'] for p in self.payments)
        else:
            return 0


class Handler(BaseRequestHandler):
    def handle(self):
        msg = self.get_message()
        if msg['client_type'] == 'client':
            self.handle_client()
        elif msg['client_type'] == 'printer':
            self.handle_printer()

    def handle_client(self):
        while True:
            msg = self.get_message()
            if msg['method'] == 'get_total_money':
                self.send_message(self.server.db.total_money)
            elif msg['method'] == 'add_payment':
                payment = {'money': msg['params']['money'],
                           'account': msg['params']['account']}
                print('Add payment: %s' % msg['params'])
                self.server.db.payments.append(payment)
                self.server.printer_queue.put(payment)
            elif msg['method'] == 'exit':
                break

    def handle_printer(self):
        while True:
            msg = self.server.printer_queue.get()
            self.send_message(msg)
            response = self.get_message()
            if response['status'] != 'OK':
                print('Printer status isn\'t OK')
                break

    def get_message(self):
        try:
            json_data = str(self.request.recv(BUFFER_SIZE), 'utf8')
            return json.loads(json_data)
        except:
            print('Cant parse stream, exit connection...')
            raise

    def send_message(self, msg):
        self.request.sendall(bytes(json.dumps(msg), 'utf8'))


class MainServer(ThreadingMixIn, TCPServer):
    def __init__(self, *args, **kwargs):
        super(MainServer, self).__init__(*args, **kwargs)
        self.db = Database()
        self.printer_queue = Queue()


if __name__ == '__main__':
    server = MainServer((SERVER_HOST, SERVER_PORT), Handler)
    ip, port = server.server_address

    server.serve_forever()
