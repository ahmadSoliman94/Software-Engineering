import re
import time
# (45,11),(41,15),(36,20)

PTS_REGEX = "\((\d*),(\d*)\)" # Regex to find points in a string


def find_area(points_str):
    ''' Function to find area of a polygon using shoelace formula'''

    points = [] # List to store points
    area = 0.0 # Variable to store area
    for xy in re.finditer(PTS_REGEX, points_str): # Find points in the string using finditer
        points.append((int(xy.group(1)), int(xy.group(2)))) # Append points to the list points . group(1) and group(2) are x and y coordinates respectively

    # iterate over the points and find area
    for i in range(len(points)):

        # a and b are two consecutive points
        a, b = points[i], points[(i + 1) % len(points)] # % len(points) is used to make sure that the last point is connected to the first point for example if there are 4 points then the last point is connected to the first point.
        area += a[0] * b[1] - a[1] * b[0] # Shoelace formula
    area = abs(area) / 2.0 # Absolute value of area divided by 2
    # print(area)


f = open("polygons.txt", "r") # Open file
lines = f.read().splitlines() # Read lines and split them
start = time.time() # Start time
for line in lines: # Iterate over lines
    find_area(line) # Call find_area function
end = time.time() # End time
print("Time taken", end - start) # Print time taken
