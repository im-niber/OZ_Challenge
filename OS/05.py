from multiprocessing import Process, Value, Lock
from django.http import HttpRequest

def counter1(snum, cnt, lock):
    lock.acquire()
    try:
        for i in range(cnt):
            snum.value += 1
    finally:
        lock.release()

def counter2(snum, cnt, lock):
    lock.acquire()
    try:
        for i in range(cnt):
            snum.value -= 1
    finally:
        lock.release()

if __name__ == '__main__':
    shared_number = Value('i', 0) # 공유 자원, i는 int라는 의미
    
    lock = Lock()

    p1 = Process(target=counter1, args=(shared_number, 5000, lock))
    p1.start()

    p2 = Process(target=counter2, args=(shared_number, 5000, lock))
    p2.start()

    p1.join()
    p2.join()

    print("num:", shared_number.value)