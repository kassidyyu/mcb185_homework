# 42ntcomp.py by Kassidy

import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	nts = []
	counts = []
	for nt in seq:
		if nt not in nts:    # allows for unexpected characters
			nts.append(nt)
			counts.append(0)
		idx = nts.index(nt)
		counts[idx] += 1
	print(name)
	for nt, n in zip(nts, counts):
		print(nt, n, n/len(seq))
	print()

"""
str.count()
print(name, end=' ')
for nt in 'ACGTN':
	print(seq.count(nt) / len(seq), end=' ')
print()
"""