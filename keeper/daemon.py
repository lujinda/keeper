#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-09 23:00:43
# Filename        : keeper/daemon.py
import sys
import os
import subprocess

class Daemon():
    def __init__(self, stdin='/dev/null', 
            stdout='/dev/null', stderr='/dev/null', root='/tmp', command=''):
        self.stdin = open(stdin, 'r')
        self.stdout = open(stdout, 'a+')
        self.stderr = open(stderr, 'a+')
        self.command = command
        os.chdir(root)

    def run(self):
        child = subprocess.Popen(self.command, shell=True, stdin = self.stdin,
                stdout = self.stdout, stderr = self.stderr)
        child.wait()

