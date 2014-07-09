#apply json.loads to each line in the file

import json
import pprint
import re
import string

def read_stream(droplet):
    '''
    read 'output.txt' json file, or similar. 

    '''

    #try regex to split, using \W for non-alphanumeric, i.e. punctuation, \s for whitespace between words

    # use * for 0 or more
    # use + for 1 or more

    p = re.compile(r'\W+') #try this simple way to start

    with open(droplet, 'r') as f:
#	data = json.dump(f)

        for line in f:
	    #string replace 'false' with False, because this is causing an error

	    #filled = string.replace(line, "null", "None")
	    #filled = string.replace(filled, "true", "True")
	    #filled = string.replace(filled, "false", "False")
	    
            data = json.loads(line) #skipkeys=True #tried adding skipkeys arg to deal with non-ascii characters (??) 

	    print type(data)
            pprint.pprint(data)
            
            #find the text part of the json object

	    
	    #parse into words

	    #words = p.split(#textpart)     #should return a list of words
            #print words
  
droplet = "snippet.txt"
read_stream(droplet)


#looks like the text part of the tweet is in the 4th level down, hashtags are 1st entry in 3rd tier (I think?)
#for hashtags could use regex with \A for start of string



#try: 
    #convert to lowercase before comparing


#compare the words to the dictionary to get the scores


#return the scores one line at a time







#Your script should print to stdout the sentiment of each tweet in the file, one numeric sentiment score per line. The first score should correspond to the first tweet, the second score should correspond to the second tweet, and so on. If you sort the scores, they won't match up. If you sort the tweets, they won't match up. If you put the tweets into a dictionary, the order will not be preserved. Once again: The nth line of the file you submit should contain only a single number that represents the score of the nth tweet in the input file!

#NOTE: You must provide a score for every tweet in the sample file, even if that score is zero. You can assume the sample file will only include English tweets and no other types of streaming messages.

#To grade your submission, we will run your program on a tweet file formatted the same way as the output.txt file you generated in Problem 1.

