'''
进程间的通信使用同一个队列，，， 但是问题是这样就变成了单线程
'''
from multiprocessing import Process, Queue
from time import sleep
def download(q):
    images = ['isabel.jpg', 'chris.jpg', 'dylan.jpg']
    for image in images:
        print("Downloading:", image)
        sleep(0.5)
        q.put(image)

def getFile(q):
    while True:   # 一直取queue里面的东西，直到取完
        try:
            file = q.get(timeout=3) # 3 seconds get the file otherwise catch the error
            print('{} saved.'.format(file))
        except:
            break

if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=download, args=(q,))
    p2 = Process(target=getFile, args=(q,))  # p1, p2 两个进程共用queue

    p1.start()
    p1.join()
    p2.start()
    p2.join()

'''
Downloading: isabel.jpg
Downloading: chris.jpg
Downloading: dylan.jpg
isabel.jpg saved.
chris.jpg saved.
dylan.jpg saved.
'''