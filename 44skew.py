# 44skew.py by Kassidy

import sys
import sequence
import gzip

def gc_comp_skew(fasta, window):
	fp = gzip.open(fasta, 'rt') # modified version of mcb185.read_fasta
	seq = []
	while True:
		line = fp.readline()
		if line == '': break
		line = line.rstrip()
		if line.startswith('>'): continue
		seq.append(line)
	seq = ''.join(seq)
	fp.close()
	window = int(window)
	subseq = seq[:window]
	for i in range(1, len(seq) - window):
		print(i, sequence.gc_comp(subseq), sequence.gc_skew(subseq))
		subseq = subseq[1:] + seq[i + window]

gc_comp_skew(sys.argv[1], sys.argv[2])