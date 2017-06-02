#! /usr/local/bin/python3

# UI Client 
import socket 
from tkinter import *

host = 'localhost' 
port = 2017
BUFFER_SIZE = 1024 
MESSAGE = "UI"

root = Tk()
root.title("Основной UI")
root.minsize(380,300)
root.resizable(width=False, height=False)
labMoney = Label(root, text="Введите номер телефона:").grid(row=1, column=2 , padx=(10,0))

entMsg = Entry(root, width=20)
entMsg.grid(row=2, column=2, padx=(10,0))
labMoney = Label(root, text="Внесено денег: 0").grid(row=8, column=2 , padx=(10,0))

tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientA.connect((host, port))
tcpClientA.sendall(bytes(MESSAGE, 'utf-8'))


def sendMsg():
	MESSAGE = entMsg.get()
	tcpClientA.sendall(bytes("Phone " + MESSAGE, 'utf-8'))

but = Button(root, text="Отправить", bg="white", fg="black", font="Arial", width=22,height=1,command=sendMsg).grid(row=4, column=2, padx=(1, 1))

root.mainloop()


#    data = tcpClientA.recv(BUFFER_SIZE)
#    print " Client2 received data:", data
#    MESSAGE = raw_input("tcpClientA: Enter message to continue/ Enter exit:")
 
# tcpClientA.close()
