#!bin/evn python
#-*-coding:utf8-*-
'''
python bceocr.py test.jpg
'''
from credential import BceCredentials
from bceocrapi import BceOCRAPI
import base64
import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')

ocr = BceOCRAPI("02fbe03acf3042a1b40e067bba1971f7", "bb1d4aafe7924fc0829fc33fa26b3347") ;


with open('public/uploads/bceocr/'+sys.argv[1], 'rb') as f:
    content = f.read()
    content = base64.b64encode(content)

#result = ocr.get_ocr_text(content, language='CHN_ENG')
result = ocr.get_ocr_text(content, language='CHN_ENG')

#result = ocr.get_ocr_line(content, language='CHN_ENG')

# result = ocr.get_ocr_char(content, language='CHN_ENG')
#计算数字个数

digitpatt = re.compile('\d')

def countdigits(s):
    return len(digitpatt.findall(s))

l = countdigits(result)

print(result+"=======数字个数："+str(l))