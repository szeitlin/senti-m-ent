__author__ = 'szeitlin'

import json
import re

def read_stream(droplet):
    '''
    read 'output.txt' json file, line by line, using a generator.

    '''

    with open(droplet, 'r') as f:
        for line in f:
            data = json.loads(line)
            yield data




def print_data(g):
    for x in g:
        print x



#droplet = "snippet.txt"
droplet = "problem_1_submission.txt"
g = read_stream(droplet)
print_data(g)
