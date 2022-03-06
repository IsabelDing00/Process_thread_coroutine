'''
多线程可以共享全局变量， 这里全局变量ticket有1000， 但是两个线程分别减了100， 200张票，最后票还有700
但是如果有个变量是money=0, 两个线程会对这个变量做很大的改动，每个money加10million， 但是最后money不会是20million，而是比200m 小很多，可能130m这样
现在python3。8 也是遇到需要做很大很大的时候会出错。因为存在->GIL全局解释器锁

分析：比如每次money+=1是有两步， n+1， 然后再赋值给。 但是可能就在线程1在做n+1的这步 但是还没给n赋值时，
    线程2 把执行权给抢走了，线程2拿到的是还没被赋值的。

---------python自带的坑的填坑法  线程同步------------
python底层会默认加锁
GIL全局解释器锁: global interpreter lock   --> 伪线程，但保证数据安全
缺点：时间延缓
拿到锁的线程才能被执行，所有线程要排队，所以叫伪线程。
在上面说到money的例子上， 因为线程run1， run2运算量太大，所以python会自动释放锁。 之前ticket的量太小，就不会释放。

------------与进程不一样------------
注意：在进程中全局变量在子线程中被复制，每个子线程自己做自己的，不会互相干扰
        不管是可变变量还是不可变类型都是一样的。
    但是进程可以做money的东西，
    进程：计算密集型
    线程：耗时操作：网上下载图片， 爬虫， i/o

------补充----
经常我们会听到老手说：“python下想要充分利用多核CPU，就用多进程”，原因是什么呢？

原因是：每个进程有各自独立的GIL，互不干扰，这样就可以真正意义上的并行执行，所以在python中，多进程的执行效率优于多线程(仅仅针对多核CPU而言)。
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