import os
import psutil

for proc in psutil.process_iter():
    try:
        if proc.pid == os.getpid():
            print(proc.name())
    except:
        pass
