#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-02-06 15:33:43
# Filename        : keeper/daemon.py
import sys
import os
import json
import subprocess

class Daemon():
    def __init__(self, stdin='/dev/null', 
            stdout='/dev/null', stderr='/dev/null', root='/tmp', command='', env = None):
        self.stdin = open(stdin, 'r')
        self.stdout = open(stdout, 'a+')
        self.stderr = open(stderr, 'a+')
        self.command = command.split()
        if env:
            self.env = os.environ.copy()
            self.env.update(self.__process_env(env))
        else:
            self.env = None

        os.chdir(root)

    def __process_env(self, env):
        return dict(map(lambda x:x.split(':', 1),
            env.split()))

    def run(self):
        child = subprocess.Popen(self.command, stdin = self.stdin,
                stdout = self.stdout, stderr = self.stderr, env = self.env)
        return child

