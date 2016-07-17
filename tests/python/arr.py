__author__ = 'feng'
from pylab import *
arr = array([[183 ,527 , 56 , 56],
 [514 ,489 , 66 , 66]
 ])



# arr = delete(arr, 0,axis=0)
# print arr
# arr_copy = arr
arr_copy = []
for index ,a in enumerate(arr):
    # arr_copy = delete(arr_copy, index,axis=0)
    # print index
    print a
    # arr_copy = np.append(arr_copy,a)
    arr_copy.append(a)

print arr_copy