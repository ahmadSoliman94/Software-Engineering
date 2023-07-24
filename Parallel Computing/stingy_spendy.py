import time
from threading import Thread, Lock


class StingySpendy:
    money = 100
    #mutex = Lock()

    def stingy(self):
        for i in range(1000000):
            #self.mutex.acquire() # acquire the lock: means that the thread is using the lock
            self.money += 10
            #self.mutex.release() # release the lock: means that the thread is done with the lock
        print("Stingy Done")

    def spendy(self):
        for i in range(1000000):
            #self.mutex.acquire()
            self.money -= 10
            #self.mutex.release()
        print("Spendy Done")


ss = StingySpendy()
Thread(target=ss.stingy, args=()).start()
Thread(target=ss.spendy, args=()).start()
time.sleep(5)
print("Money in the end", ss.money)
