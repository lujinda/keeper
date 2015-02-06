#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-02-06 15:24:36
# Filename        : keeper/worker.py
# Description     : 
#from multiprocessing.process import Process
from threading import Thread
from keeper.daemon import Daemon
from keeper.config import get_program_list
import os
import time
import signal
from functools import partial

# 把daemon的环境传进去
class Worker(Thread):
    def __init__(self, program):
        Thread.__init__(self);
        self.program = program

    def listen_daemon(self, daemon):
        restart_count = 0
        while (not self._task_stop) and restart_count <= int(self.program['restart_num']):
            self.task = daemon.run()
            self._run_time = int(time.time())
            self.task.wait()
            restart_count += 1

    def run(self):
        self._task_stop = False
        kwargs = self.program.copy()
        map(kwargs.pop, ['name', 'restart_num'])
        daemon = Daemon(**kwargs)
        self.listen_daemon(daemon)

    def task_restart(self):
        self.task_stop()
        self.task_start()

    def task_start(self):
        if self.task_status == 'STOP':
            return
        self.run()

    def _send_signal(self, sig):
        if self.task_status == 'STOP':
            return
        self._task_stop = True
        self.task.send_signal(sig)
        self.task.wait()
        self.task.poll = True

    def task_stop(self):
        self._send_signal(signal.SIGTERM)
    
    def task_kill(self):
        self._send_signal(signal.SIGKILL)

    @property
    def task_pid(self):
        return self.task.pid

    @property
    def task_name(self):
        return self.program['name']
    
    @property
    def task_ttl(self):
        if self.task_status != 'STOP':
            return int(time.time()) - self._run_time

    @property
    def task_status(self):
        return (self._task_stop or self.task.poll()) and 'STOP'  or 'RUN'

def made_worker_list():
    worker_list = []
    for program in get_program_list():
        worker_list.append(Worker(program))

    return worker_list

