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
    
    afinnfile.close()

    return scores


def compare(tweetwords, scores):
    '''
    look up individual words(str) in the scores_dict 
    returns a list of scores (int) 
   
    >>>compare['accused', 'effective', 'wanker']
    [-1, +1, -3]

    '''

    scorelist = []

    for word in tweetwords:
        if word in scores.keys():
           scorelist.append(scores[word])

    print scorelist
    return scorelist

scores = scores_to_dict()
tweetwords = ['accused', 'effective', 'wanker']
scorelist = compare(tweetwords, scores)
