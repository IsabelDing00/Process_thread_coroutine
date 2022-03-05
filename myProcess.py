'''
自定义进程
'''
from multiprocessing import Process
class MyProcess(Process):
    def __init__(self, name):
        super(MyProcess, self).__init__()
        self.name = name

    # override
    def run(self):
        n = 1
        while True:
            print('{0}---->, n: {1}'.format(n, self.name))
            n += 1

if __name__ == '__main__':
    p1 = MyProcess('Isabel')
    p1.start()

    p2 = MyProcess('Chris')
    p2.start()
