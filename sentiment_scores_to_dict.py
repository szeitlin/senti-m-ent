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


scores_to_dict()
