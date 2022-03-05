'''
全局变量在子线程中被复制，每个子线程自己做自己的，不会互相干扰
不管是可变变量还是不可变类型都是一样的
'''

import os
from multiprocessing import Process
from time import sleep

m = 1  # 不可变类型
# list=[]   # 可变类型
def task1(second):
    global m
    while True:
        sleep(second)
        m += 1
        print("------This is task1------", m)

def task2(second):
    global m
    while True:
        sleep(second)
        m += 1
        print("------This is task2------", m)

number = 1
if __name__ == '__main__':
    print(os.getppid())
    p1 = Process(target=task1, name="Process 1", args=(1,))
    p1.start()
    p2 = Process(target=task2, name="Process 2", args=(2,))
    p2.start()

'''
20724
------This is task1------ 2
------This is task2------ 2
------This is task1------ 3
------This is task1------ 4
------This is task2------ 3
------This is task1------ 5
------This is task1------ 6
------This is task2------ 4
------This is task1------ 7
'''