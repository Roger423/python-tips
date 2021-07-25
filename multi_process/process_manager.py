from multiprocessing import Process

class MyProcess(Process):
    def __init__(self, func, q, args):
        super(MyProcess, self).__init__()
        self.func = func
        self.args = args
        self.res = None
        self.q = q

    def run(self):
        self.res = self.func(*self.args)
        self.q.put(self.res)





