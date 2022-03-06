'''
协程：微线程， 主要由生成器来做
'''
import time


def task1():
    for i in range(3):
        print('A' + str(i))
        yield
        time.sleep(1)

def task2():
    for i in range(3):
        print('B' + str(i))
        yield
        time.sleep(2)

if __name__ == '__main__':
    t1 = task1()
    t2 = task2()

    while True:
        try:
            next(t1)
            next(t2)
        except:
            break

'''
A0
B0
A1
B1
A2
B2
'''
