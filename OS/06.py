import threading
from multiprocessing import Process, Value, Lock

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

    # 스레드에서도 lock 걸지 않으면 동기화 문제가 발생한다~
    t1 = threading.Thread(target=counter1, args=(shared_number, 10000, lock))
    t1.start()

    t2 = threading.Thread(target=counter2, args=(shared_number, 2222, lock))
    t2.start()

    t1.join()
    t2.join()

    print("num:", shared_number.value)