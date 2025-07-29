# 65translate.py by Kassidy

import mcb185
import argparse

parser = argparse.ArgumentParser(description='mRNA translator.')
parser.add_argument('file', type=str, help='fasta file of mRNAs')		       
parser.add_argument('-m', '--min', type=int, default=100,
	help='minimum protein length [%(default)i]')
parser.add_argument('-a', '--anti', action='store_true', 
	help='also examine the anti-parallel strand')
arg = parser.parse_args()

for defline, seq in mcb185.read_fasta(arg.file):
	# immediately check if sequence is too short first
	if len(seq)//3 < arg.min: continue
	for i in range(len(seq)):
		if seq[i:i+3] == 'ATG': # translate at first start codon
			aas = mcb185.translate(seq, i)
			break
	# mcb.translate will continue after *
	stop = aas.find('*') # find first stop codon
	aas = aas[:stop]     # cut off translation there
	# another check for minimum length
	if len(aas) < arg.min: continue
	print('>', defline, sep='')
	# print the protein seq with line length 60
	for i in range(0, len(aas)-59, 60):
		print(aas[i:i+60])
	if len(aas) % 60 != 0:
		print(aas[i+60 : i+60 + len(aas) % 60])

	# repeat for anti-parallel strand if anti flag
	if not arg.anti: continue
	# same process ater finding anti-parallel seq using mcb185 again
	anti_seq = mcb185.anti_seq(seq)
	for i in range(len(anti_seq)):
		if anti_seq[i:i+3] == 'ATG':
			aas = mcb185.translate(anti_seq, i)
			break
	stop = aas.find('*')
	aas = aas[:stop]
	if len(aas) < arg.min: continue
	print('>', defline, ' anti', sep='') # mark as 'anti'
	for i in range(0, len(aas)-59, 60):
		print(aas[i:i+60])
	if len(aas) % 60 != 0:
		print(aas[i+60:i+60+len(aas) % 60])