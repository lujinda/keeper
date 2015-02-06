#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-02-05 21:43:49
# Filename        : keeper/sock/server.py
# Description     : 

from SocketServer import UnixStreamServer, StreamRequestHandler, ThreadingMixIn
from keeper.sock.session import Session
import os


class KeeperServer(ThreadingMixIn, UnixStreamServer):
    allow_reuse_address = True
    
class KeeperSocketHandler(StreamRequestHandler):
    def handle(self):
       session = Session(self.rfile, self.wfile, self.server.worker_list)

class Server():
    def __init__(self, unix_file, worker_list):
        self._server = KeeperServer(unix_file, KeeperSocketHandler)
        self._server.worker_list = worker_list

    def run(self):
        self._server.serve_forever()
    
