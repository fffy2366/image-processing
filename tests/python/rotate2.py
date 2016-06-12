#encoding:utf-8
import numpy as np
import cv2
image = cv2.imread("/Users/fengxuting/Downloads/1463815812385A98C108.jpg")

'''
[openCV—Python(5)——	图像几何变换](http://blog.csdn.net/jnulzl/article/details/47057673)
'''
# cv2.imshow("Original",image)
# cv2.waitKey(0)
(h,w) = image.shape[:2]
center = (w / 2,h / 2)

#旋转45度，缩放0.75
# M = cv2.getRotationMatrix2D(center,45,0.60)#旋转缩放矩阵：(旋转中心，旋转角度，缩放因子)
# rotated = cv2.warpAffine(image,M,(w,h))
# cv2.imshow("Rotated by 45 Degrees",rotated)
# cv2.waitKey(0)
#旋转-45度，缩放1.25
# M = cv2.getRotationMatrix2D(center,-45,1.25)#旋转缩放矩阵：(旋转中心，旋转角度，缩放因子)
# rotated = cv2.warpAffine(image,M,(w,h))
# cv2.imshow("Rotated by -90 Degrees",rotated)
# cv2.waitKey(0)

#90 -90 10度一个图
for i in range(-90,100,10):
    print(i)
    M = cv2.getRotationMatrix2D(center,i,0.60)#旋转缩放矩阵：(旋转中心，旋转角度，缩放因子)
    rotated = cv2.warpAffine(image,M,(w,h))
    cv2.imshow("Rotated by 45 Degrees",rotated)
    cv2.waitKey(0)
