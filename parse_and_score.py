#apply json.loads to each line in the file

import json
import pprint
import re
import string

def read_stream(droplet):
    '''
    read 'output.txt' json file, or similar. 

    '''

    p = re.compile(r'\W+') 

    with open(droplet, 'r') as f:
        for line in f:
            data = json.loads(line) 

	    #print type(data)
            #pprint.pprint(data)
            
	    tweet = data['text']
	    
	    #parse into words

	    words = p.split(tweet)     #should return a list 
            print words 		
  
droplet = "snippet.txt"
read_stream(droplet)


#for hashtags could use regex with \A for start of string?


#try: 
    #convert to lowercase before comparing


#compare the words to the dictionary to get the scores


#return the scores one line at a time







#Your script should print to stdout the sentiment of each tweet in the file, one numeric sentiment score per line. The first score should correspond to the first tweet, the second score should correspond to the second tweet, and so on. If you sort the scores, they won't match up. If you sort the tweets, they won't match up. If you put the tweets into a dictionary, the order will not be preserved. Once again: The nth line of the file you submit should contain only a single number that represents the score of the nth tweet in the input file!

#NOTE: You must provide a score for every tweet in the sample file, even if that score is zero. You can assume the sample file will only include English tweets and no other types of streaming messages.

#To grade your submission, we will run your program on a tweet file formatted the same way as the output.txt file you generated in Problem 1.

