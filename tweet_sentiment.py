
import json
import re
import sys

def scores_to_dict(sent_file):
    '''
    Parses the given tab-delimited text file, and returns a dictionary of words mapped to sentiment scores (as integers).

    accused -2
    assured 2
    returns:
    {accused:-2, assured:2}
    '''

    #with open(sent_file, 'r') as afinnfile:

    scores = {}

    for line in sent_file:
            term, score  = line.split("\t")
            scores[term] = int(score)

    return scores

def read_stream(tweet_file):
    '''
    read 'output.txt' json file, line by line, using a generator.

    '''

    for line in tweet_file:
        data = json.loads(line)
        yield data

def split_stream(data):
    '''
    find the tweets in the lines of json objects, and split them into word lists.

    '''
    p = re.compile(r'\W+')

    for x in data:
        try:
            tweet = x['text']
            tweetobj = p.split(tweet)     #should return a list
            yield tweetobj

        except KeyError:
            pass


def convert_and_compare(tweetobj, scores):
    '''
    for each word, everything ascii and lowercase
    look up individual word(str) in the scores_dict
    returns a list of scores (int)

    '''

    for wordlist in tweetobj:
        scorelist = []
        for word in wordlist:
            word = word.encode('ascii', 'ignore') #change from unicode to be able to operate on strings
            word = word.lower()			          #get rid of capital letters
            if word in scores.keys():
                scorelist.append(scores[word])
            else:
                scorelist.append(0)
        result = sum(scorelist)
        #print scorelist
        yield result

def print_result(result):
    for x in result:
        print x

def hw(tweet_file, sent_file):
    data = read_stream(tweet_file)
    tweetobj = split_stream(data)
    scores = scores_to_dict(sent_file)
    result = convert_and_compare(tweetobj, scores)
    print_result(result)

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(tweet_file, sent_file)
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()







#Your script should print to stdout the sentiment of each tweet in the file, one numeric sentiment score per line. The first score should correspond to the first tweet, the second score should correspond to the second tweet, and so on. If you sort the scores, they won't match up. If you sort the tweets, they won't match up. If you put the tweets into a dictionary, the order will not be preserved. Once again: The nth line of the file you submit should contain only a single number that represents the score of the nth tweet in the input file!

#NOTE: You must provide a score for every tweet in the sample file, even if that score is zero. You can assume the sample file will only include English tweets and no other types of streaming messages.

#To grade your submission, we will run your program on a tweet file formatted the same way as the output.txt file you generated in Problem 1.

