# Unit 1 Assessment by Kassidy

import math

# 1. A function that computes the distance between 2 points on a graph
def distance(x1, y1, x2, y2): # given points (x1, y1) and (x2, y2)
    return math.sqrt((x1-x2)**2 + (y2-y1)**2)

# 2. A function that returns the omplement of a DNA letter, None if not DNA
def dna_complement(nt): # taken from 10demo.py, allows for lowercase
    if   (nt == 'A') or (nt == 'a'): return 'T'
    elif (nt == 'T') or (nt == 't'): return 'A'
    elif (nt == 'C') or (nt == 'c'): return 'G'
    elif (nt == 'G') or (nt == 'g'): return 'C'

# 3. Return the maximum of 3 numbers
def max3(a, b, c): # also taken from 10demo.py
    if a >= b and a >= c: return a
    elif a >= b and a < c: return c
    else: return b

# I think PHRED quality scores are in log10 because probabilities are in 
# decimals, so using base 10 matches up with our number system.
# To modify for base 2, the formula would be different.

# Modified 12phred.py for log2
def char_to_prob(char):
    return 2 ** ((33 - ord(char))/2)

def prob_to_char(p):
    score = -2*math.log2(p)
    if math.isclose(math.floor(score), score): # ensures score is an integer 
        return chr(math.floor(score) + 33)
    elif math.isclose(math.ceil(score), score): # check rounding both ways
        return chr(math.ceil(score) + 33)