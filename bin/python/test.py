#!usr/bin/python
# -*-coding:utf8-*-

import datetime
import re
import numpy as np
import sys
datetime.datetime.now()

print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
def test():
    y = 2001
    i = 3
    print (y>2000)
    if y>2000 and y <5000:
        print i,y,3
test()

def countdigits(s):
    digitpatt = re.compile('\d')

    return len(digitpatt.findall(s))

#print countdigits("f . 1")>4


x = np.array([1,2,3,4,3,2,4,3])
y = x.tolist()
print y.count(3)

data = [
[121.1, 0.02, 0.02],
[121.1, 0.05, 0.05],
[122.1, 0.56, 0.6],
[122.1, 3.79, 4.04],
[123.1, 93.75, 100.0],
[123.1, 0.01, 0.01],
[124.1, 0.01, 0.01],
[124.1, 1.01, 1.08],
[124.1, 0.11, 0.11],
[124.1, 0.05, 0.06],
[125.1, 0.39, 0.41],
]
from itertools import groupby
print [reduce(lambda x,y: [k, x[1]+y[1], x[2]+y[2]], rows) for \
k, rows in groupby(data, lambda x: x[0])]


a = np.array([[1,2,3,4,5,6,7],[1,2,3,4,3,5,5],[3,4,2,3,2,2,3],[5,4,3,2,3,6,7]])

a.shape = 1,-1
print a[0].tolist().count(2)
sys.exit(0)



total = 0
for i in a:
    total += i.tolist().count(2)

# print total
# print a.tostring()

# print a.groupby(a[0]).sum()

for i in groupby(a, lambda x: x[0]):
    print i

print sum(a,1)

def count(start=0, step=1):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
    n = start
    while True:
        yield n
        n += step
print count(10)