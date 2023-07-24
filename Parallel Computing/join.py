import time
from threading import Thread

def child():
    print('Child thread Doing Work>>>>>')
    time.sleep(4)

    print('Child thread Done... ')




def parent():

     
    t = Thread(target=child, args=())
    t.start() # start the child thread
    
    print('Parent thread is Waiting>>>>>')
    t.join() # lock the parent thread until the child thread is done.
    print('Parent thread is unblock... ')



parent()