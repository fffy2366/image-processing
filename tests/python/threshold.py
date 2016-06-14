#!bin/evn python
# -*-coding:utf8-*-
'''
0x02. cv.Threshold
cv.Threshold(src, dst, threshold, maxValue, thresholdType)

函数 cvThreshold 对单通道数组应用固定阈值操作。

该函数的典型应用是对灰度图像进行阈值操作得到二值图像。

参数说明：

全选复制放进笔记src：原始数组 (单通道 , 8-bit of 32-bit 浮点数)。
dst：输出数组，必须与 src 的类型一致，或者为 8-bit。
threshold：阈值
maxValue：使用 CV_THRESH_BINARY 和 CV_THRESH_BINARY_INV 的最大值。
threshold_type：阈值类型
threshold_type=CV_THRESH_BINARY:
    如果 src(x,y)>threshold ,dst(x,y) = max_value; 否则,dst（x,y）=0;
threshold_type=CV_THRESH_BINARY_INV:
    如果 src(x,y)>threshold,dst(x,y) = 0; 否则,dst(x,y) = max_value.
threshold_type=CV_THRESH_TRUNC:
    如果 src(x,y)>threshold，dst(x,y) = max_value; 否则dst(x,y) = src(x,y).
threshold_type=CV_THRESH_TOZERO:
    如果src(x,y)>threshold，dst(x,y) = src(x,y) ; 否则 dst(x,y) = 0.
threshold_type=CV_THRESH_TOZERO_INV:如果 src(x,y)>threshold，dst(x,y) = 0 ; 否则dst(x,y) = src(x,y).
'''
import cv2.cv as cv
# image = cv.LoadImage('../../public/images/skew-linedetection.png')
image = cv.LoadImage('/Users/fengxuting/Downloads/test122.jpg')

new = cv.CreateImage(cv.GetSize(image), image.depth, 1)
cv.ShowImage('a_window', new)
cv.WaitKey(0)
for i in range(image.height):
    for j in range(image.width):
        new[i,j] = max(image[i,j][0], image[i,j][1], image[i,j][2])

cv.Threshold(new, new, 10, 255, cv.CV_THRESH_BINARY_INV)
cv.ShowImage('b_window', new)
cv.WaitKey(0)