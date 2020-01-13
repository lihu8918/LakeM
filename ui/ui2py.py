#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 09:02:19 2017

@author: Administrator
"""
import glob
import os

ui_files = glob.glob('./*.ui')

for ui_file in ui_files:
    py_file = ui_file.replace('.ui', '.py')
    cmd = 'pyuic5 -o ' + py_file + ' ' + ui_file
    os.system(cmd)

os.system('pyrcc5 -o res.py res.qrc')