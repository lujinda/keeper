#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-02-06 15:23:23
# Filename        : keeper/daemon.py
import sys
import os
import json
import subprocess

class Daemon():
    def __init__(self, stdin='/dev/null', 
            stdout='/dev/null', stderr='/dev/null', root='/tmp', command='', env = '{}'):
        self.stdin = open(stdin, 'r')
        self.stdout = open(stdout, 'a+')
        self.stderr = open(stderr, 'a+')
        self.command = command.split()
        self.env = os.environ.copy()
        self.env.update(self.__process_env(env))
        os.chdir(root)

    def __process_env(self, env):
        return dict(map(lambda x:x.split(':', 1),
            env.split()))

    def run(self):
        child = subprocess.Popen(self.command, stdin = self.stdin,
                stdout = self.stdout, stderr = self.stderr)
        return child

