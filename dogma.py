# 11oligo.py edited
# used in 60demo.py

def tm(seq): # accept a string
	nts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
	for nt in seq: # assumes only 'ATGC' in seq
		if   nt == 'A': nts['A'] += 1
		elif nt == 'T': nts['T'] += 1
		elif nt == 'G': nts['G'] += 1
		else:           nts['C'] += 1
	nt_total = nts['A'] + nts['T'] + nts['G'] + nts['C']
	if nt_total <= 13: 
		return (nts['A'] + nts['T'])*2 + (nts['G'] + nts['C'])*4 # formula 1
	else:
		return 64.9 + 41*(nts['G'] + nts['C'] - 16.4) / nt_total # formula 2
