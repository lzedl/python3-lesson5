#! /usr/local/bin/python3

# Cash input Client 
import socket 
from tkinter import *

host = 'localhost'
port = 2017
BUFFER_SIZE = 1024 
MESSAGE = "Cash_input"

tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientA.connect((host, port))
tcpClientA.sendall(bytes(MESSAGE, 'utf-8'))


def sendMsg100():
    tcpClientA.sendall(bytes("Money 100", 'utf-8'))


def sendMsg500():
    tcpClientA.sendall(bytes("Money 500", 'utf-8'))


def sendMsg1000():
    tcpClientA.sendall(bytes("Money 1000", 'utf-8'))


def sendMsg5000():
    tcpClientA.sendall(bytes("Money 5000", 'utf-8'))


def sendMsg50():
    tcpClientA.sendall(bytes("Money 50", 'utf-8'))

root = Tk()
root.title("Купюроприемник")
root.minsize(300,300)
root.resizable(width=False, height=False)

but50 = Button(root, text="Внести 50 руб", bg="white", fg="black", font="Arial", width=22,height=1, command=sendMsg50).grid(row=1, column=2, padx=(1, 1))
but100 = Button(root, text="Внести 100 руб", bg="white", fg="black", font="Arial", width=22,height=1, command=sendMsg100).grid(row=2, column=2, padx=(1, 1))
but500 = Button(root, text="Внести 500 руб", bg="white", fg="black", font="Arial", width=22,height=1, command=sendMsg500).grid(row=3, column=2, padx=(1, 1))
but1000 = Button(root, text="Внести 1000 руб", bg="white", fg="black", font="Arial", width=22,height=1, command=sendMsg1000).grid(row=4, column=2, padx=(1, 1))
but5000 = Button(root, text="Внести 5000 руб", bg="white", fg="black", font="Arial", width=22,height=1, command=sendMsg5000).grid(row=5, column=2, padx=(1, 1))


root.mainloop()

