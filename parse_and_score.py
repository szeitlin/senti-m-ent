#apply json.loads to each line in the file

import json
import pprint
import re
import string

def scores_to_dict():
    '''
    Parses the given tab-delimited text file, and returns a dictionary of words mapped to sentiment scores (as integers).

    accused -2
    assured 2
    returns:
    {accused:-2, assured:2}
    '''

    with open("AFINN-111.txt", 'r') as afinnfile:

        scores = {} 

        for line in afinnfile:
                term, score  = line.split("\t")  
                scores[term] = int(score)  
    #print scores.items() # Print every (term, score) pair in the dictionary as one big list

    #write dict to a file
        
    with open("scores_dict.py", 'w') as f:
        f.seek(0)
        scored = str(scores) #convert from dict to avoid buffer error
        f.write(scored)
    
    afinnfile.close()
    f.close()

    return scores 

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

            try:
	        tweet = data['text']
	        words = p.split(tweet)     #should return a list 
		print words
    	        continue

 	    except KeyError:
		continue
  
#for hashtags could use regex with \A for start of string?

def convert_and_compare(words, scores):
    '''
    for each word, everything ascii and lowercase
    look up individual word(str) in the scores_dict
    returns a list of scores (int)

    '''
    scorelist = []

    #convert to lowercase before comparing
    for word in words:
        word = word.encode('ascii', 'ignore') #change from unicode to be able to operate on strings
        word = word.lower()			#get rid of capital letters
        if word in scores.keys():
           scorelist.append(scores[word])

    print scorelist
    return scorelist

#droplet = "snippet.txt"
#droplet = "testfile_other.txt"
droplet = "problem_1_submission.txt"
words = read_stream(droplet)
#scores = scores_to_dict()	
#scorelist = convert_and_compare(words, scores)


#sum the scores


#return the scores one line at a time







#Your script should print to stdout the sentiment of each tweet in the file, one numeric sentiment score per line. The first score should correspond to the first tweet, the second score should correspond to the second tweet, and so on. If you sort the scores, they won't match up. If you sort the tweets, they won't match up. If you put the tweets into a dictionary, the order will not be preserved. Once again: The nth line of the file you submit should contain only a single number that represents the score of the nth tweet in the input file!

#NOTE: You must provide a score for every tweet in the sample file, even if that score is zero. You can assume the sample file will only include English tweets and no other types of streaming messages.

#To grade your submission, we will run your program on a tweet file formatted the same way as the output.txt file you generated in Problem 1.

