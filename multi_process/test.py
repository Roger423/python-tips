import multiprocessing as mp
from multiprocessing import Process


class MyProcess(Process):
    """
    自定义多进程，继承自原生Process,目的是获取多进程结果到queue
    """

    def __init__(self, func, args, q):
        super(MyProcess, self).__init__()
        self.func = func
        self.args = args
        self.res = ''
        self.q = q
        # self._daemonic = True
        # self._daemonic = True

    def run(self):
        self.res = self.func(*self.args)
        self.q.put((self.func.__name__, self.res))


def use_multiprocessing(func_list):
    # os.system('export PYTHONOPTIMIZE=1') # 解决 daemonic processes are not allowed to have children 问题
    q = mp.Queue()  # 队列,将多进程结果存入这里，进程间共享， 多进程必须使用 multiprocessing 的queue
    proc_list = []
    res = []
    for func in func_list:
        proc = MyProcess(func['func'], args=func['args'], q=q)
        proc.start()
        proc_list.append(proc)

    for p in proc_list:
        p.join()
    while not q.empty():
        r = q.get()
        res.append(r)
    return res

use_multiprocessing()