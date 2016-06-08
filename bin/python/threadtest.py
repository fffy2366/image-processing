#!bin/evn python
# -*-coding:utf8-*-
import threading, time


def doWaiting():
    print 'start waiting:', time.strftime('%H:%M:%S')
    time.sleep(60)
    print 'stop waiting', time.strftime('%H:%M:%S')

for i in range(0,10):
    thread1 = threading.Thread(target=doWaiting)
    thread1.start()


time.sleep(1)  # 确保线程thread1已经启动
print 'start join'
thread1.join()  #
