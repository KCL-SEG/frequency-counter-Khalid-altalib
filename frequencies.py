"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

from collections import Counter
def frequencies(items):

    strings = [str(x) for x in items] # convert all items to strings
    frequencies = Counter(strings) # count the frequencies of each string
    #print(frequencies)

    return frequencies

#frequencies(['0', 4,4,'4','d','d','e',0,'a','d','4'])
