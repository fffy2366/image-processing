from PIL import Image
import pytesseract
import re
import sys

#print(pytesseract.image_to_string(Image.open('src/test-european.jpg'), lang='fra'))
str = pytesseract.image_to_string(Image.open('public/uploads/ocr/'+sys.argv[1]),lang='eng', boxes=False, config="-psm 6") ;
#str = pytesseract.image_to_string(Image.open('public/uploads/ocr/'+sys.argv[1]),lang='chi_sim', boxes=False, config="-psm 6") ;
#str = pytesseract.image_to_string(Image.open('public/uploads/ocr/'+sys.argv[1]),lang='num', boxes=False, config="-psm 6") ;

print(str)
ret = re.findall("\d{5,12}",str)
print len(ret)