from PIL import Image
import pytesseract
import re
#print(pytesseract.image_to_string(Image.open('test.png')))
qq_str = pytesseract.image_to_string(Image.open('images/qq.gif')) ;
#qq_str = pytesseract.image_to_string(Image.open('images/p8.jpg')) ;
#qq_str = pytesseract.image_to_string(Image.open('p2.jpg')) ;
print(qq_str)
#print(pytesseract.image_to_string(Image.open('src/test-european.jpg'), lang='fra'))
ret = re.findall("\d{5,12}",qq_str)
print len(ret)