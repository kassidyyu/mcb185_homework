# 53dust.py by Kassidy

import argparse
import mcb185
import math

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-s', '--size', type=int, default=20, 
	help='window size [%(default)i]') # advertise default in usage statement
parser.add_argument('-e', '--entropy', type=float, default=1.4, 
	help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
arg = parser.parse_args() # harvest values on command line and assig to variable properties
print('dusting with', arg.file, arg.size, arg.entropy, arg.lower)

# taken from 46dust.py with edited variable names

for defline, seq in mcb185.read_fasta(arg.file):
	output = []
	subseq = seq[:arg.size]
	for i in range(len(seq) - arg.size + 1):
		a = subseq.count('A')
		c = subseq.count('C')
		g = subseq.count('G')
		t = subseq.count('T')
		n_comp = [a / arg.size, c / arg.size, g / arg.size, t / arg.size]
		e_calc = 0
		for val in n_comp:
			if val == 0: continue
			e_calc -= val * math.log2(val)
		if i == 0:
			if e_calc < arg.entropy:
				output[:arg.size] = ['N'] * arg.size
			else:
				for i in range(arg.size):
					output.append(subseq[i])
		else:
			if e_calc >= arg.entropy:
				output.append(subseq[-1])
			elif output[-1] == 'N' and e_calc < arg.entropy:
				output.append(subseq[-1])
			else:
				output[i:i + arg.size] = ['N'] * arg.__sizeof__
		if i != len(seq) - arg.size:
			subseq = subseq[1:] + seq[i + arg.size]

with open('dust_output.txt', 'w') as outfile:
	print('>', defline, sep='', file=outfile)
	for i in range(0, len(output) -59, 60):
		print(''.join(output[i:i + 60]), file=outfile)
	if len(output) % 60 != 0:
		print(''.join(output[i + 60:i + 60 + len(output) % 60]), file=outfile)