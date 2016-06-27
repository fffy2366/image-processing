#!bin/evn python
# encoding:utf-8
__author__ = 'feng'
import re

class StringUtils:
    #统计数字个数
    def countdigits(self,s):
        digitpatt = re.compile('\d')

        return len(digitpatt.findall(s))

    #4-12位连续数字
    def digits(self,s):
        # s = "12aaaaa22222dsfsdf"
        ret = re.findall("\d{4,12}",s)
        return ret