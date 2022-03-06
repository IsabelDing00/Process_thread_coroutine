'''
线程比进程的开销小，和进程很类似
1， 线程是进程中的一个实体
2，线程和其他线程共享进程所拥有的全部资源
3， 同一进程中，多个线程可以并发执行（轮流着用）， 但可能出现间断性


--------多线程 multithreading--------
需要硬件支持， 多核心处理器
状态： 新建， 就绪， 运行， 阻塞， 结束
优点：把占据长时间的程序中的任务放到后台处理
    用户界面可以更吸引人， 比如用户点击一个按钮出发一个时间的处理， 可以弹出一个进度条来显示处理的进度
    程序运行速度可能加快
    在用户输入，文件读写，网络收发数据等很有用， ->可以释放一些内存等。

--------线程code--------
import threading

'''
import threading
from time import sleep

def downLoad(n):
    images = ['isabel.jpg', 'chris.jpg', 'dylan.jpg']
    for image in images:
        print("Downloading:", image)
        sleep(n)       #这里sleep就是一种阻塞
        print("Download {} successed".format(image))

def listenMusic():
    musics = ["hihi", "haha", "liangliang"]
    for music in musics:
        sleep(0.5)
        print("Listening to", music)

if __name__ == '__main__':
    # 线程对象
    t1 = threading.Thread(target=downLoad, name='test1', args=(1,))
    t1.start()

    t2 = threading.Thread(target=listenMusic, name='test2',)
    t2.start()

'''
Downloading: isabel.jpg
Listening to hihi
Download isabel.jpg successed
Downloading: chris.jpg
Listening to haha
Listening to liangliang
Download chris.jpg successed
Downloading: dylan.jpg
Download dylan.jpg successed


线程1 ------- ｜————————｜      线程1和2不会一起进到cpu里， 谁阻塞了，谁就把这个资源让给其他的线程。 没有顺序，不是按照1-2-3。
             ｜  cpu   ｜
线程2 ------- ｜————————｜
'''
