#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-09 22:58:25
# Filename        : keeper/config.py
# Description     : 
import ConfigParser, os

cfg_file = ['keeper.cfg', '/etc/keeper.cfg']

def get_program_list():
    program_list = []
    cfg = ConfigParser.ConfigParser()
    for f in cfg_file:
        if not os.path.exists(f):
            continue
        cfg.read(f)
        for section in cfg.sections():
            program = dict(cfg.items(section))
            program_list.append(program)

        return program_list

    raise Exception('keeper.cfg does not exist')

