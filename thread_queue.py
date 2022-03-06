'''
可以使用queue来实现线程间的同步
'''

#通过queue的方式进行线程间同步，Queue在底层通过实现了dqueue(双生队列，在字节码时实现了线程安全)实现了线程安全
from queue import Queue

import time
import threading
# 先爬文章列表页， 爬到的放到queue里面  -> queue.put()
def get_detail_url(queue):
    # 爬取文章列表页
    while True:
        print("get detail url started")
        time.sleep(4)
        for i in range(20):
            queue.put("http://projectsedu.com/{id}".format(id=i))#没有多余的位置时，会一直阻塞在这，直到有空闲的位置
        print("get detail url end")

# 要拿文章列表页， 就去queue里面取    -> queue.get()
def get_detail_html(queue):
    #爬取文章详情页
    while True:
        url = queue.get()# 如果没有数据会一直阻塞在这
        # for url in detail_url_list:
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")



#1. 线程通信方式- 共享变量

if  __name__ == "__main__":
    detail_url_queue = Queue(maxsize=1000)


    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_queue,))
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_queue,))
        html_thread.start()
    start_time = time.time()

    detail_url_queue.task_done() # 队列任务完成，只有调用这个，线程才会退出
    detail_url_queue.join() # 阻塞主线程，调用了task_done，queue才会退出，不然一直会阻塞在queue这

    #当主线程退出的时候， 子线程kill掉
    print ("last time: {}".format(time.time()-start_time))