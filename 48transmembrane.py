# 48transmembrane.py by Kassidy

import sys
import mcb185

# dictionary based on Wikipedia Kyte-Doolittle scale hydropathy scores
KD = {
	'I' : 4.5,	'V' : 4.2,	'L' : 3.8,	'F' : 2.8,	'C' : 2.5,	'M': 1.9,
	'A' : 1.8,	'G' : -.4,	'T' : -.7,	'S' : -.8,	'W' : -.9,	'Y' : -1.3,
	'H' : -3.2,	'E' : -3.5,	'Q' : -3.5,	'D' : -3.5,	'N' : -3.5,	'K' : -3.9,
	'R' : -4.5
	}

for defline, protein in mcb185.read_fasta(sys.argv[1]):
	if len(protein) < 41: continue
	subseq = protein[:8] # initialize first potential signal
	signal = False
	# 8 long so look through first 22 for signal peptide in first 30 aa's
	for i in range(23): 
		if 'P' in subseq:                  # no proline in signal peptides
			if i == 22: break   	       # last loop, iteration will fail
			subseq = subseq[1:] + protein[i + 8]
			continue                       # skip calculation
		kd_sum = 0                         # initialize/reset sum to 0
		for aa in subseq: kd_sum += KD[aa] # sum scores
		if kd_sum / 8 >= 2.5:              # found signal peptide
			signal = True
			break                          # stop looping
		if i < 22: subseq = subseq[1:] + protein[i + 8]
	if not signal: continue # no signal, move onto next protein
	# repeat similar process to look for transmembrane regions
	region = protein[30:41]
	tm_reg = False
	for i in range(30, len(protein) - 10): # windows of 11, look through rest
		if 'P' in region:                  # no proline
			if i == len(protein) - 11: break
			region = region[1:] + protein[i + 11]
			continue
		kd_sum = 0
		for aa in region: kd_sum += KD[aa]
		if kd_sum / 11 >= 2.0:             # found transmembrane region
			tm_reg = True
			break
		if i < len(protein) - 11: region = region[1:] + protein[i + 11]
	if tm_reg: print(defline[:60])         # print name of transmembrane