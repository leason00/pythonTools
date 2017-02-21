#!/usr/bin/python
# -*- coding: UTF-8 -*-
import subprocess
import commands
import os

# aaa = commands.getoutput("java")
# # bbb = commands.getstatus("echo 'lll'")
# print aaa
# # print bbb
aaa = 'nihao'
# bbb = os.system('leason.bat '+aaa)
bbb = commands.getoutput('leason.bat '+aaa)
print bbb