import time
from multiprocessing import Process

def do_work():
    print("Starting Work")
    i = 0
    for _ in range(20000000):
        i+=1
    print("Finishing Work")
    



if __name__ == '__main__':
    
    for _ in range (5):
        p  = Process(target=do_work , args=())
        p.start()
        #do_work()