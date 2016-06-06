# -*- coding: utf-8 -*-
__author__ = 'feng'
path = "/Users/fengxuting/Downloads/ocr3.png"

from PIL import Image, ImageDraw

im = Image.open(path)
im = im.convert('L')

# 二值化
print 'img info:', im.format, im.size, im.mode
width, height = im.size
for x in xrange(width):
    for y in xrange(height):
        p = im.getpixel((x, y))
        if p > 90:
            im.putpixel((x, y), 255)
        else:
            im.putpixel((x, y), 0)

# 去头去尾
mlist = set([])
p = im.load()
for x in xrange(width):
    for y in xrange(height):
        p = im.getpixel((x, y))
        if p < 200:
            mlist.add(x)

mlist = list(mlist)
left = mlist[:1][0]
right = mlist[len(mlist) - 1:][0]

box = (left, 0, right, height)
im = im.crop(box)

width, height = im.size
ps = [0] * width

for x in xrange(width):
    for y in xrange(height):
        p = im.getpixel((x, y))
        if p == 0:
            ps[x] = ps[x] + 4

image = Image.new('RGB', (200, 200), (255, 255, 255))
draw = ImageDraw.Draw(image)
ps_width = len(ps)
for k in xrange(ps_width):
    source = (k, 199)  # 起点坐标y=99, x=[0,1,2....]
    target = (k, 199 - ps[k])  # 终点坐标y=255-a[x],a[x]的最大数值是200,x=[0,1,2....]
    draw.line([source, target], (100, 100, 100), 1)

#image.show()
im.show()
