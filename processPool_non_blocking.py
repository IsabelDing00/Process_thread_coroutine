'''
如果子进程有很多， 那就用multiProcessing 的pool
初始化pool时， 可以指定一个最大进程数。
如果进程没满， 可以直接创建新的进程
如果pool满了，需要等到pool中有进程结束了才能开新的进程
优点：可以重复利用进程

两种类型：      阻塞blocking：pool.apply(func, args=)
                    pool没有复用。必须要一个做完了才能做另外一个。
        非阻塞non-blocking: pool.apply_async(fun, args=)   ----> 最大化的利用CPU
                            所有进程全部添加到队列。7个进程在一个只有5个进程的pool里。
                            一口气先做5个，哪个做完了就用哪个进程ID做还在排队的。
                            一个进程任务做完了就会调用回掉函数。

必须要用的code：
    from multiprocessing import Pool
    pool = Pool(n)
    pool.apply()  or pool.apply_async()
    pool.close()
    pool.join()

'''
import time
import os
from random import random
from multiprocessing import Pool
# 非阻塞式进程
def task1(task_name):
    print("Start task:", task_name)
    start = time.time()
    time.sleep(random() * 2)
    end = time.time()
    return "The process {} last{}: Process id:{}".format(task_name, (end - start), os.getpid())

def callback_func(n):
    print(n)

if __name__ == '__main__':
    pool = Pool(5)   # a pool with 5 process
    tasks = ["Shopping", "Move", "Eating", "Traveling", "Partying", "Walking", "Studying"]
    for task in tasks:
        pool.apply_async(task1, args=(task,), callback=callback_func())

    pool.close()  # 添加任务结束
    pool.join()  # 如果我不加这两行就会直接打印 over!!!!!

    print("over!!!!")

'''
Start task: Shopping
Start task: Move
Start task: Eating
Start task: Traveling
Start task: Partying     -> 一共7个任务， 但是pool只有5个
The process Move last0.38276100158691406: Process id:26168    -> move干完了， 做walking
Start task: Walking
The process Shopping last0.5154731273651123: Process id:26167
Start task: Studying
The process Partying last0.5044400691986084: Process id:26171
The process Traveling last0.5174510478973389: Process id:26170
The process Studying last0.8832869529724121: Process id:26167
The process Walking last1.3542556762695312: Process id:26168
The process Eating last1.7945358753204346: Process id:26169
over!!!!
'''