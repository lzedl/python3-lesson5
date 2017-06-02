#! /usr/local/bin/python3
from tkinter import *
from client import Client
from settings import *


class MainWindow(Tk):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.title('Основной UI')
        self.minsize(380, 300)
        self.resizable(width=False, height=False)

        self.label = Label(self, text='Введите номер аккаунта:')
        self.label.grid(row=1, column=2, padx=(10, 0))

        self.account_edit = Entry(self, width=20)
        self.account_edit.grid(row=2, column=2, padx=(10, 0))

        self.money_btn = Button(self, text='Отправить',
                                bg='white', fg='black',
                                font='Arial', width=22, height=1,
                                command=self.send_money)
        self.money_btn.grid(row=4, column=2, padx=(1, 1))

        self.client = Client(SERVER_HOST, SERVER_PORT)

    def send_money(self):
        self.client.send_message({
            'method': 'add_payment',
            'params': {'money': 10,
                       'account': self.account_edit.get()}
        })


def main():
    root = MainWindow()
    root.mainloop()


if __name__ == '__main__':
    main()
