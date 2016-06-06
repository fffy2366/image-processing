import sys, PIL.Image as Image

img = Image.open('test112.jpg').convert('YCbCr')
w, h = img.size
data = img.getdata()
cnt = 0
for i, ycbcr in enumerate(data):
    y, cb, cr = ycbcr
    print y
    if 86 <= cb <= 117 and 140 <= cr <= 168:
        cnt += 1
print '%s %s a porn image.' % ('myphoto7.jpg', 'is' if cnt > w * h * 0.3 else 'is not')
