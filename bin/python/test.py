#!usr/bin/python
# -*-coding:utf8-*-

import datetime
import re

datetime.datetime.now()

print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def countdigits(s):
    digitpatt = re.compile('\d')

    return len(digitpatt.findall(s))

#print countdigits("f . 1")>4


