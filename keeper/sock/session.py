#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-02-06 15:29:35
# Filename        : keeper/sock/session.py
# Description     : 
from keeper.worker import Worker

class Session():
    def __init__(self, rfile, wfile, worker_list):
        # 一些不希望让别人看到的命令都用_开头
        self._rfile = rfile
        self._wfile = wfile
        self._worker_list = worker_list
        self.start()

    def do_list(self, _):
        """list worker"""
        list_template = "%-5s%-20s%-10s%-10s%s"
        response = [ list_template % ('No', 'Name', 'Pid',
            'Status', 'TTL(seconds)')]
        for i, worker in enumerate(self._worker_list):
            response.append(list_template %(i, 
                worker.task_name, worker.task_pid, worker.task_status,  worker.task_ttl))

        self.write_lines(response)

    def do_stop(self, No):
        """stop No"""
        No = int(No)
        self._worker_list[No].task_stop()
        self.write_line('Ok')

    def do_kill(self, No):
        """kill No"""
        No = int(No)
        self._worker_list[No].task_kill()
        self.write_line('Ok')

    def do_start(self, No):
        """start No"""
        No = int(No)
        if self._worker_list[No].task_status == 'STOP':
            worker = self._worker_list.pop(No)
            new_worker = Worker(worker.program)
            print new_worker
            self._worker_list.insert(No, new_worker)
            new_worker.start()
        self.write_line('Ok')


    def do_restart(self, No):
        """restart No"""
        No = int(No)
        self.do_stop(No)
        self.do_start(No)

    def start(self):
        while True:
            line = self.read_line()
            if not line:
                break
            command, args = (line.split(' ', 1) + [''])[:2]
            try:
                func = getattr(self, 'do_' + command.strip())
                func(args)
            except (AttributeError, ValueError):
                self.do_help(args)
                continue

    def do_help(self, _):
        """Show Help"""
        help_content = []
        for key in dir(self):
            if not key.startswith('do_'):
                continue
            obj = getattr(self, key)
            if not callable(obj):
                continue
            help_content.append(obj.__doc__)

        self.write_lines(help_content)

    def write(self, data):
        self._wfile.write(data)
        self.flush()

    def read(self):
        return self._rfile.read()

    def read_line(self):
        return self._rfile.readline()

    def write_line(self, data):
        self.write(data + '\n')

    def write_lines(self, lines):
        self.write_line('\n'.join(lines))

    def flush(self):
        self._wfile.flush()

