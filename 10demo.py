# 10demo.py by Kassidy

import math
"""
print("hello, again") # greeting
print(1.5e-2)
print(32 // 5)
print(math.ceil(7/3))
print(math.floor(7/3))
print(0.1 * 3)

def pythagoras(a, b):
	return math.sqrt(a**2 + b**2)

print(pythagoras(3, 4))

s = 'hello world'
print(s, type(s))

a = 1
b = 1.0
c = a == b
print(c)
print(type(c))
"""

# Practice Functions

def is_integer(n): return n % 1 == 0

def is_probability(p): return p >= 0 and p <= 1

def dna_molecular_weight(nt):
	if   nt == 'A': return 135.13
	elif nt == 'T': return 126.1133
	elif nt == 'C': return 111.1
	elif nt == 'G': return 151.13

def dna_complement(nt):
	if   nt == 'A': return 'T'
	elif nt == 'T': return 'A'
	elif nt == 'C': return 'G'
	elif nt == 'G': return 'C'

def maximum(a, b, c):
	if a >= b and a >= c: return a
	elif a >= b and a < c: return c
	else: return b

def sensitivity(tp, fp, tn, fn):
	return tp / (tp + fn)

def specificity(tp, fp, tn, fn):
	return tn / (tn + fp)

def f1_score(tp, fp, tn, fn):
	recall = sensitivity(tp, fp, tn, fn)
	precision = tp / (tp + fp)
	return (2 * precision * recall) / (precision + recall)

def shannon_entropy(A, C, G, T):
	nt_count = A + C + G + T
	running_sum = 0
	if A != 0: running_sum -= (A / nt_count) * math.log2(A / nt_count)
	if C != 0: running_sum -= (C / nt_count) * math.log2(C / nt_count)
	if G != 0: running_sum -= (G / nt_count) * math.log2(G / nt_count)
	if T != 0: running_sum -= (T / nt_count) * math.log2(T / nt_count)
	return running_sum