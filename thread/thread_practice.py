'''
    * thread
        - 동시에 여러 프로세스가 실행되게 하는 것
'''

import threading

class Massenger(threading.Thread) :
    def run(self) :
        for _ in range(10) :
            print(threading.currentThread().getName())


x = Massenger(name = "메세지를 보냅니다")
y = Massenger(name = "메세지를 수신합니다")

x.start()
y.start()