from multiprocessing import Process
import os
import time

def writer():
    print(f'{os.getpid()}가 파일에 write')
    with open('04.txt', 'w') as f:
        f.write("Hello")

def reader():
    print(f'{os.getpid()}가 파일에 read')
    with open('04.txt', 'r') as f:
        print(f.read())


if __name__ == '__main__':
    p1 = Process(target=writer)
    p1.start()

    time.sleep(2) # 쓰기가 끝나야 함

    p2 = Process(target=reader)
    p2.start()

    p1.join()
    p2.join()