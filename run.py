#!/usr/bin/python3
# coding=utf-8

# copyright : (C) © 2023 - KhamdihiXD
# file name : run.py
# Note      : Jangan di edit bro

import os
import sys
from item import main

author = ['khamdihiXD.']
if sys.version_info.major == 2:
   quit('\nGunakan python3 untuk menjalankan.. run ( python3 {} )'.format(sys.argv[0]))

def install(module):
    return os.system('pip3 install {}'.format(module))

try:
    import requests
except ModuleNotFoundError:
    install('requests')
try:
    import bs4
except ModuleNotFoundError:
    install('bs4')
try:
    import rich
except ModuleNotFoundError:
    install('rich')

def update():
    os.system('git pull')
    try:os.system('cls') if 'win' in sys.platform else os.system('clear')
    except:pass
    main.asset(author[0].replace('.','')).Login('/cokie.js')

if __name__ == '__main__':
   update()
