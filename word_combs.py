#!/usr/bin/env python

"""
athenahealth coding challenge
Friday December 20, 2013
Alex Lehman

Run by entering 'python challenge.py <word>'' at command line
"""

import sys
import math

def num_comb(word):
    
    length = len(word)
    
    # Base case
    if length == 0:
        return 1
    
    # Word in alphabetical order
    sortd = ''.join(sorted(word))
    
    # Sorted string of the unique letters in given word
    unique = ''.join(sorted(list(set(sortd))))
    
    # Number of appearances of each unique letter in the word
    appearances = []
    # Factorials of appearances of words to calculate total permutations later
    denom_vals = []
    for i in unique:
        n = sortd.count(i)
        appearances.append(n)
        denom_vals.append(math.factorial(n))
        
    # Calculate the total possible combinations of a word with the given letters
    total_combs = math.factorial(length)/(reduce(lambda x,y:x*y, denom_vals))
    
    index = unique.index(word[0])
    
    # If first letter is the first alphabetically of all unique letters
    if index == 0:
        # No combinations before it need to be accounted for
        # so continue on to counting the number of combinations for rest of word
        return 0 + num_comb(word[1:])
    
    # Account for previous combinations that begin with first letter
    # and move on to the next letter by recursive call to count the rest
    else:
        return total_combs/length*sum(appearances[:unique.index(word[0])]) + num_comb(word[1:])
if __name__ == '__main__':

	w = sys.argv[1]
	print num_comb(w)



