'''
死锁
如果两个线程分别占有一部分资源并且等待对方的资源，就会造成死锁
一旦发生会造成应用的停止响应，程序不会做任何事

避免死锁：
1。在acquire()里面加入timeout
'''
from threading import Thread, Lock
import time
lockA = Lock()
lockB = Lock()

class MyThread1(Thread):
    def run(self):
        if lockA.acquire():
            print(self.name+'get lock A')
            time.sleep(0.1)
            if lockB.acquire(timeout=5):
                print(self.name+'get lock B and A')
                lockB.release()
            lockA.release()

class MyThread2(Thread):
    def run(self):
        if lockB.acquire():
            print(self.name+'get lock B')
            time.sleep(0.1)
            if lockA.acquire(timeout=5):
                print(self.name+'get lock B and A')
                lockA.release()
            lockB.release()

if __name__ == '__main__':
    t1 = MyThread1()
    t2 = MyThread2()

    t1.start()
    t2.start()



'''
class MyThread1(Thread):
    def run(self):
        if lockA.acquire():
            print(self.name,'get lock A')
            time.sleep(0.1)
            if lockB.acquire():
                print(self.name,'get lock B and A')
                lockB.release()
            lockA.release()

class MyThread2(Thread):
    def run(self):
        if lockB.acquire():
            print(self.name,'get lock A')
            time.sleep(0.1)
            if lockA.acquire():
                print(self.name,'get lock B and A')
                lockA.release()
            lockB.release()
产生死锁： 
Thread-1 get lock A
Thread-2 get lock A
'''