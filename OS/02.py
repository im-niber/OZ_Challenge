import os
from multiprocessing import Process
import threading
import time

def funcc():
    print(" test func ")
    print("pid:", os.getpid())
    print("my parent pid:", os.getppid())

def thread_func():
    print("hi thread func")
    print("pid:", os.getpid())
    print('스레드 아이디:', threading.get_native_id())

def something(word):
    while True:
        print(word)
        time.sleep(2)

if __name__ == '__main__':
    print("base pid:", os.getpid())
    child1 = Process(target=funcc)
    child1.start()
    child2 = Process(target=funcc)
    child2.start()
    child3 = Process(target=funcc)
    child3.start()

    thread1 = threading.Thread(target=thread_func)
    thread1.start()

    t = threading.Thread(target=something, args =('happy', ))
    t.daemon = True # 메인 스레드의 기능이 끝나면 나도 끝나겠다 ~ 라는 의미
    print('메인 스레드 for start')
    t.start()

    while True:
        try:
            print("daily...")
            time.sleep(1)
        except KeyboardInterrupt:
            print("end")
            break
