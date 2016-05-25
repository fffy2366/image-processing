#!bin/evn python
#-*-coding:utf8-*-

from credential import BceCredentials
from bceocrapi import BceOCRAPI
import base64
import sys

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

print(result)