import time 
import json
from urllib.request import urlopen, Request as request
from threading import Thread


finish_counting = 0 # global variable to keep track of the number of threads that have finished counting

def count_letters(url, freq):


    response = request(url,headers={'User-Agent': 'Mozilla/5.0'}) # User-Agent is required to avoid 403: Forbidden error. 'Mozilla/5.0' is a standard User-Agent
    txt = str(urlopen(response).read()) # read the response and convert it into string

    # iterate through the string
    for l in txt:
        letter = l.lower() # convert all letters to lower case
        if letter in freq: # if the letter is already in the dictionary, increment its count
            freq[letter] += 1 # count the letter

    global finish_counting # use the global variable
    finish_counting += 1 # increment the number of threads that have finished counting



def main():

    freq = {} # create an empty dictionary
    
    # iterate through the alphabet
    for c in 'abcdefghijklmnopqrstuvwxyz':
        freq[c] = 0 # initialize dictionary with all letters and set their count to 0

    start_time = time.time() # start the timer

    # iterate through the RFCs
    for i in range(1000,1020): 

        # create a thread for each RFC
        t = Thread(target=count_letters, args=['http://www.rfc-editor.org/rfc/rfc{}.txt'.format(i), freq]).start() # call the count_letters function

        # count_letters('http://www.rfc-editor.org/rfc/rfc{}.txt'.format(i), freq) # call the count_letters function

    while finish_counting < 10:
        time.sleep(0.5) # sleep for 0.5 seconds

    end_time = time.time() # end the timer

    print(json.dumps(freq, indent=4)) # print the dictionary , indent=4 is used to print the dictionary in a readable format
    print('Done', 'Time taken: {}'.format(end_time - start_time)) # print the time taken to run the program


if __name__ == '__main__':
    main()

