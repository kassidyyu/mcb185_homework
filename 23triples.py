# 23triples.py by Kassidy

import math

def triples(n): # n is the maximum side length
    a = 3       # start with the smallest triple
    b = 4
    print(a, b, math.sqrt(a**2 + b**2))
    for i in range(n - 4):
        b = a + 1
        a += 1
        for i in range(n - a - 1):
            b += 1
            c = math.sqrt(a**2 + b**2)
            if c % 1 == 0: print(a, b, c)

triples(100)