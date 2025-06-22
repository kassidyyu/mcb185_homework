# Unit 3 Practice Problems by Kassidy

import math

# Minimum value of a list
def minimum(list):
    minimum = list[0]
    for element in list:
        if element < minimum: mimimum = element
    return minimum

# minimum & max
def minmax(list):
    minimum = list[0] # initialize to first element
    maximum = list[0]
    for element in list:
        if element < minimum:   minimum = element
        elif element > maximum: maximum = element
    return minimum, maximum

# mean of values
def mean(list):
    sum = 0
    for element in list: sum += element
    return sum / len(list)

# entropy of probability distribution
def entropy(dist):
    prob_sum = 0
    sum = 0
    for p in dist: 
        if p > 0 and p < 1:
            sum -= p * math.log2(p)
            prob_sum += p
    if math.isclose(prob_sum, 1): return sum

# Kullback-Leibler distance between two sets of distributions
def dkl(dist1, dist2):
    sum = 0
    for p1, p2 in zip(dist1, dist2):
        sum += p1 * math.log2(p1 / p2)
    return sum
