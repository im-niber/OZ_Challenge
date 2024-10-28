from multiprocessing import Process, Pipe
import os

# conn: 누구랑 통신할지에 대한 연결
def send(conn):
    print(f"{os.getpid()}가 {os.getppid()}에게 데이터를 보냅니다")
    conn.send("hihi parent!")
    conn.close()

if __name__ == "__main__":
    parent, child = Pipe() # 생성자함수로, 튜플형태로 커넥션 두 개를 반환함
    p = Process(target=send, args=(child, ))
    p.start()
    print('기존 프로세스 아이디:', os.getpid())
    print(parent.recv()) # 요게 없다면, 부모 프로세스가 뭘 받는지 보이지 x
    p.join() # 프로세스가 작업을 종료할때까지 기다림
