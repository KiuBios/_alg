# 設置 timeout 為 5秒 ， 如果超時則判斷該程式不會停機

from multiprocessing import Process
import time

timeout = 5  # 限時 5 秒

def halt(func, *args, **kwargs):
    p = Process(target=func, args=args, kwargs=kwargs)
    p.start()
    p.join(timeout)
    if p.is_alive():
        p.terminate()  # 強制終止進程
        return False
    else:
        return True
    
def f1(n):
    return n * n

def f2(n):
    s = 0
    for _ in range(n):
        for _ in range(n):
            for _ in range(n):
                for _ in range(n):
                    s = s+1

if __name__ == '__main__':
    print('halt(f1,3)=', halt(f1, 3))
    print('halt(f2,10)=', halt(f2, 10))
    print('halt(f2,1000)=', halt(f2, 1000))
