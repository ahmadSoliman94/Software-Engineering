import time
from threading import Thread

def do_work():
    print("Starting Work")
    i = 0
    for _ in range(200000000):
        i+=1
    print("Finishing Work")
    



if __name__ == '__main__':
    
    for _ in range (5):
        t  = Thread(target=do_work , args=())
        t.start()
        #do_work()