#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-02-06 13:07:20
# Filename        : keeper/panel.py
# Description     : 
import os
from keeper.sock.server import Server
import atexit

class Panel():
    """
    管理面板程序
    """
    def __init__(self, worker_list):
        unix_file = '/tmp/keeper.sock'
        atexit.register(os.remove, unix_file)
        if os.path.exists(unix_file):
            os.remove(unix_file)
        self._server = Server(unix_file, worker_list)

    def run(self):
        self._server.run()

