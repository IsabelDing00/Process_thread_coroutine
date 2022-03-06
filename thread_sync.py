'''
线程同步： 一个一个完成，一个做完另一个才能进来， 但效率会很低
使用thread里面的lock 和rlock 可以实现简单的线程同步，这两个对象都有acquire方法和release方法
lock.acquire()
lock.release()
'''
import threading
import time
from time import sleep
import random

lock = threading.Lock()
list1 = [0] * 10
def task1():
    # 获取线程锁， 如果已经上锁就需要等待锁的释放
    lock.acquire()
    for i in range(len(list1)):
        list1[i] = 1
        sleep(0.5)

    lock.release()

def task2():
    lock.acquire()
    for i in range(len(list1)):
        print('---->', list1[i])
        sleep(0.5)
    lock.release()

if __name__ == '__main__':
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)

    t1.start()
    t2.start()

'''
----> 1
----> 1
----> 1
----> 1
----> 1
----> 1
----> 1
----> 1
----> 1
----> 1
'''