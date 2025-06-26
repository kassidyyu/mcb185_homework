# 46dust.py by Kassidy

import sys
import mcb185
import math

window = int(sys.argv[2])
threshold = float(sys.argv[3])

with open('masked_regions.txt', 'w') as outfile:
	for defline, seq in mcb185.read_fasta(sys.argv[1]):
		outfile.write(defline)
		outfile.write('\n')
		subseq = seq[:window]
		a = subseq.count('A')
		c = subseq.count('C')
		g = subseq.count('G')
		t = subseq.count('T')
		n_comp = [a / window, c / window, g / window, t / window]
		for i in range(1, len(seq) - window + 1):
			entropy = 0
			for val in n_comp:
				if val == 0: continue
				entropy -= val * math.log2(val)
			if i == len(seq) - window: # last iteration
				if entropy < threshold: outfile.write('N' * window)
				else: outfile.write(subseq)
				break
			if entropy < threshold: outfile.write('N')
			else: outfile.write(subseq[0])
			if i % 60 == 0: outfile.write('\n')			
			subseq = subseq[1:] + seq[i + window]
			a = subseq.count('A')
			c = subseq.count('C')
			g = subseq.count('G')
			t = subseq.count('T')
			n_comp = [a / window, c / window, g / window, t / window]

# debug: needs to replace whole region with N's