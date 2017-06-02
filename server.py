#! /usr/local/bin/python3

import socket 
import threading
import socketserver 


class payTerm():
    def __init__(self):
        self.Money = 0
        self.Phone = '+7 000 000-00-00'

payment = payTerm()
        

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = str(self.request.recv(1024), 'utf-8')
        if data == 'Printer':
            self.request.sendall(str(payment.Money))
            self.request.sendall(str(payment.Phone))

        while True:
            data = str(self.request.recv(1024), 'utf-8')
            if not data:
                break
            elif data[0:5] == 'Phone':
                payment.Phone = data[6:]
                print("Указан номер телефона", payment.Phone)
            elif data[0:5] == 'Money':
                payment.Money = payment.Money + int(data[6:])
                print("Внесенная сумма", payment.Money)
            cur_thread = threading.current_thread()
            print("Сервер получил сообщение:{}".format(data))
            response = bytes("{}: {}".format(cur_thread.name, data), 'utf-8')
            #self.request.sendall(response)


# Обратите внимание на использование класса-примеси ThreadingMixIn
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """ 
        Потоковый сервер. Достаточно создать класс без "внутренностей"
    """
    pass

if __name__ == "__main__":

    TCP_IP = 'localhost' 
    TCP_PORT = 2017 
    BUFFER_SIZE = 1024 

    server = ThreadedTCPServer((TCP_IP, TCP_PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:", server_thread.name)
    while True:
        pass
    server.shutdown()
    server.server_close()
