'''
如果子进程有很多， 那就用multiProcessing 的pool
初始化pool时， 可以指定一个最大进程数。
如果进程没满， 可以直接创建新的进程
如果pool满了，需要等到pool中有进程结束了才能开新的进程
优点：可以重复利用进程

两种类型： 阻塞blocking：pool.apply(func, args=)
                    pool没有复用。添加一个进程，执行一个。必须要一个做完了才能做下一个。
        非阻塞non-blocking: pool.apply_async(func, args=)
                所有进程全部添加到队列。7个进程在一个只有5个进程的pool里。
                一口气先做5个，哪个做完了就用哪个进程ID做还在排队的。
                一个进程任务做完了就会调用回掉函数。


必须要用的code：
    from multiprocessing import Pool
    pool = Pool(n)
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
    print("The process {} last{}: Process id:{}".format(task_name,(end - start), os.getpid()))

# def callback_func(n):
#     print(n)

if __name__ == '__main__':
    pool = Pool(5)   # a pool with 5 process
    tasks = ["Shopping", "Move", "Eating", "Traveling", "Partying", "Walking", "Studying"]
    for task in tasks:
        pool.apply(task1, args=(task,))

    pool.close()  # 添加任务结束
    pool.join()  # 如果我不加这两行就会直接打印 over!!!!!

    print("over!!!!")

'''
Start task: Shopping
The process Shopping last1.2641878128051758: Process id:26488   
Start task: Move
The process Move last1.7846899032592773: Process id:26490
Start task: Eating
The process Eating last0.9538109302520752: Process id:26489
Start task: Traveling
The process Traveling last0.4757881164550781: Process id:26491
Start task: Partying
The process Partying last0.3553440570831299: Process id:26492
Start task: Walking
The process Walking last0.7980489730834961: Process id:26488
Start task: Studying
The process Studying last1.3714587688446045: Process id:26490
over!!!!
'''