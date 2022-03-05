'''
进程
优点：稳定性高， 一个进程崩溃不会影响其他的进程
缺点：创建进程开销大， 进程数量有限

# create a process
# linux can use fork to create process
# Windows use Multiprocessing
代码：

from multiprocessing import Process

process = Process(target=函数, name=进程的名字, args=(给函数传递的参数)
process.start()启动进程并执行任务
process.run() 只是执行任务但是不启动进程
terminate()终止

'''


import os
from multiprocessing import Process
from time import sleep

def task1(second,name):
    while True:
        sleep(second)
        print("------This is task1------", os.getpid(), '------', os.getppid(), name)

def task2(second,name):
    while True:
        sleep(second)
        print("------This is task2------", os.getpid(), '------', os.getppid(), name)

number = 1
if __name__ == '__main__':
    print(os.getppid())
    p1 = Process(target=task1, name="Process 1", args=(1,'aa'))
    p1.start()
    p2 = Process(target=task2, name="Process 2", args=(2,'bb'))
    p2.start()

    while True:
        number += 1
        sleep(0.2)
        if number == 50:
            p1.terminate()
            p2.terminate()
            break
        else:
            print(number)

    print("Process ends.")

'''
task 1 and task will be my two sub process under parent pid 20724
20724 -> ppid()
------This is task1------ 21041(pid()) ------ 21039(ppid()) aa
------This is task1------ 21041 ------ 21039 aa
------This is task2------ 21042 ------ 21039 bb
------This is task1------ 21041 ------ 21039 aa
------This is task1------ 21041 ------ 21039 aa
------This is task2------ 21042 ------ 21039 bb
------This is task1------ 21041 ------ 21039 aa
'''