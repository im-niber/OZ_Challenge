import os
from multiprocessing import Process

def funcc():
    print(" test func ")
    print("pid:", os.getpid())
    print("my parent pid:", os.getppid())

if __name__ == '__main__':
    print("01.py pid:", os.getpid())
    child1 = Process(target=funcc)
    child1.start()
    child2 = Process(target=funcc)
    child2.start()
    child3 = Process(target=funcc)
    child3.start()
