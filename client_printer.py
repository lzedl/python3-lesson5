#! /usr/local/bin/python3

# Printer Client 
import socket 
from tkinter import *
import threading
import socketserver 

# host = 'localhost' 
# port = 2017
# BUFFER_SIZE = 1024 
MESSAGE = "Printer"

# tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# tcpClientA.connect((host, port))
# tcpClientA.sendall(bytes(MESSAGE, 'utf-8'))

# root = Tk()
# root.title("Принтер")
# root.minsize(300,300)
# root.resizable(width=False, height=False)

# output = Text(root, bg="white", font="Arial 12", width=50, height=10)
# output.grid(row=1, column=1,  columnspan=7)

# while True:
#     root.update_idletasks()
#     root.update()
#     response = str(tcpClientA.recv(1024), 'utf-8')
#     output.insert("0.0", str(response) + "\n")
#     print("Сервер ответил: {}".format(response))


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

	def handle(self):
		

		# self.request.sendall(MESSAGE)
		# self.request.sendall(TCP_IP)
		# self.request.sendall(str(TCP_PORT))
		while True:
			data = str(self.request.recv(1024), 'utf-8')
			output.insert("0.0", str(data) + "\n")

        
# Обратите внимание на использование класса-примеси ThreadingMixIn
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """ 
        Потоковый сервер. Достаточно создать класс без "внутренностей"
    """
    pass

if __name__ == "__main__":

	TCP_IP = 'localhost' 
	TCP_PORT = 2018 
	BUFFER_SIZE = 1024 

	#server = ThreadedTCPServer((TCP_IP, TCP_PORT), ThreadedTCPRequestHandler)
	#ip, port = server.server_address

	# Start a thread with the server -- that thread will then start one
	# more thread for each request
	#server_thread = threading.Thread(target=server.serve_forever)
	# Exit the server thread when the main thread terminates
	#server_thread.daemon = True
	#server_thread.start()
	#print("Printer running in thread:", server_thread.name)
	tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	tcpClientA.connect(('localhost', 2017))
	tcpClientA.sendall(bytes(MESSAGE, 'utf-8'))
	tcpClientA.sendall(bytes(TCP_IP, 'utf-8'))
	tcpClientA.sendall(bytes(str(TCP_PORT), 'utf-8'))

	root = Tk()
	root.title("Принтер")
	root.minsize(300,300)
	root.resizable(width=False, height=False)

	output = Text(root, bg="white", font="Arial 12", width=50, height=10)
	output.grid(row=1, column=1,  columnspan=7)

	root.mainloop()
    # while True:
    #     pass
    # server.shutdown()
    # server.server_close()
     