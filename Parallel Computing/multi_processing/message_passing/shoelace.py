import re
import time
from multiprocessing import Process, Queue
# (45,11),(41,15),(36,20)

PTS_REGEX = "\((\d*),(\d*)\)" # Regex to find points in a string
TOTAL_PROCESSES = 8  # Number of processes to spawn


def find_area(points_queue):

    ''' Function to find area of a polygon using shoelace formula'''


    points_str = points_queue.get() # Get points from queue and store it in points_str
    while points_str is not None:  # Iterate until points_str is not None
        points = [] # List to store points
        area = 0.0 # Variable to store area
        for xy in re.finditer(PTS_REGEX, points_str): # Find points in the string using finditer
            points.append((int(xy.group(1)), int(xy.group(2)))) # Append points to the list points . group(1) and group(2) are x and y coordinates respectively

        for i in range(len(points)): # iterate over the points and find area
            a, b = points[i], points[(i + 1) % len(points)] # a and b are two consecutive points. % len(points) is used to make sure that the last point is connected to the first point for example if there are 4 points then the last point is connected to the first point.
            area += a[0] * b[1] - a[1] * b[0] # Shoelace formula
        area = abs(area) / 2.0 # Absolute value of area divided by 2
        # print(area)
        points_str = points_queue.get() # Get points from queue and store it in points_str if points_str is None then loop will break


if __name__ == '__main__':
    queue = Queue(maxsize=1000) # Create a queue with maxsize 1000 
    processes = [] # List to store processes
    for i in range(TOTAL_PROCESSES): # Iterate over TOTAL_PROCESSES
        p = Process(target=find_area, args=(queue,)) # p is a process which will call find_area function and pass queue as an argument
        processes.append(p) # Append p to processes list
        p.start()  # Start the process
    f = open("polygons.txt", "r")  # Open file
    lines = f.read().splitlines() # Read lines and split them
    start = time.time() # Start time
    for line in lines: # Iterate over lines
        queue.put(line) # Put line in queue
    for _ in range(TOTAL_PROCESSES): queue.put(None) # Put None in queue, this will make sure that all processes will stop
    for p in processes: p.join() # Wait for all processes to finish p.join() will block the main process until p is finished
    end = time.time()
    print("Time taken", end - start)
