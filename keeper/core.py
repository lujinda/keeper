#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-02-05 18:02:30
# Filename        : keeper/core.py
# Description     :  让worker_list中的worker工作起来

from keeper.worker import made_worker_list
from keeper.panel import Panel

class Keeper():
    def __init__(self):
        self.worker_list = made_worker_list()

    def run(self):
        for worker in self.worker_list:
            worker.start()

        panel = Panel(self.worker_list)
        panel.run()

