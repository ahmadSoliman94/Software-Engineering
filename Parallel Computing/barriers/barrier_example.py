import time
from threading import Barrier, Thread

barrier = Barrier(2) # create a barrier that waits for 2 threads, that is, the barrier will wait for 2 threads to reach the barrier before it is released. 


def wait_on_barrier(name, time_to_sleep):
    for i in range(10):
        print(name, "running")
        time.sleep(time_to_sleep)
        print(name, "is waiting on barrier")
        barrier.wait()
    print(name, "is finished")


red = Thread(target=wait_on_barrier, args=["red", 4]) # create a thread that calls the wait_on_barrier function with the name "red" and sleeps for 4 seconds
blue = Thread(target=wait_on_barrier, args=["blue", 10]) # create a thread that calls the wait_on_barrier function with the name "blue" and sleeps for 10 seconds
red.start()
blue.start()
# time.sleep(8)
# print("Aborting barrier")
# barrier.abort()
# barrier.reset()
