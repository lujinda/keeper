#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-02-06 13:54:06
# Filename        : bin/keeper-panel.py
# Description     : 

import socket
import sys
from threading import Thread
BLOCK_SIZE = 4096


def exec_command(func):
    def wrap(self, *args, **kwargs):
        func(self, *args, **kwargs)
        data = self.read()
        self.show(data)
    return wrap

class Panel():
    def __init__(self):
        self._client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self._client.connect('/tmp/keeper.sock')
    @exec_command
    def send_command(self, command):
        self.write_line(command)

    def show(self, data):
        sys.stdout.write(data)

    def write(self, data):
        self._client.sendall(data)

    def write_line(self, data):
        self.write(data + '\n')

    def read(self):
        _t = self._client.recv(BLOCK_SIZE)
        return _t

    def start(self):
        self.send_command('list')
        loop_thread = Thread(target= self.loop)
        loop_thread.start()

    def loop(self):
        while True:
            command = raw_input('> ').strip()
            if command in ['q', 'quite']:
                self._client.close()
                break
            self.send_command(command)

if __name__ == "__main__":
    panel = Panel()
    panel.start()

