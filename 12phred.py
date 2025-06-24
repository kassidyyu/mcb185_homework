# 12phred.py by Kassidy

import math

def char_to_prob(char):
	return 10 ** ((33 - ord(char))/10)

def prob_to_char(p):
	score = -10*math.log10(p)
	if math.isclose(math.floor(score), score): # ensures score is an integer 
		return chr(math.floor(score) + 33)
	elif math.isclose(math.ceil(score), score): # check rounding both ways
		return chr(math.ceil(score) + 33)

print(char_to_prob('A'))
print(prob_to_char(0.001))
print(prob_to_char(0.00346972491))