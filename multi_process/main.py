from func import func1, func2
from process_manager import MyProcess
from multiprocessing import Queue

def main():
    queue = Queue(2)
    p1 = MyProcess(func1, queue, args=(4, 2))
    p2 = MyProcess(func2, queue, args=(3,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res_list = list()
    while not queue.empty():
        res_list.append(queue.get())
    print(res_list)

if __name__ == '__main__':
    main()
