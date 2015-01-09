#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-09 22:58:07
# Filename        : keeper/worker.py
# Description     : 
from multiprocessing.process import Process
from keeper.daemon import Daemon
from keeper.config import get_program_list
import os

# 把daemon的环境传进去
class Worker(Process):
    def __init__(self, program):
        Process.__init__(self);
        self.program = program
    def run(self):
        daemon = Daemon(**self.program)
        daemon.run()

def made_worker_list():
    worker_list = []
    for program in get_program_list():
        worker_list.append(Worker(program))

    return worker_list

