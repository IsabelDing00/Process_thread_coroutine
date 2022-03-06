'''
多线程可以共享全局变量， 这里全局变量ticket有1000， 但是两个线程分别减了100， 200张票，最后票还有700

与进程不一样
注意：在进程中全局变量在子线程中被复制，每个子线程自己做自己的，不会互相干扰
        不管是可变变量还是不可变类型都是一样的
'''
ticket = 1000

import threading
def run1():
    global ticket
    for i in range(100):
        ticket -= 1

def run2():
    global ticket
    for i in range(200):
        ticket -= 1


if __name__ == '__main__':
    # 创建线程
    t1 = threading.Thread(target=run1, name='ticket_selling1')
    t2 = threading.Thread(target=run2, name='ticket_selling2')

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print(ticket)

'''
ticket : 700
'''