# 47cdsfinder.py by Kassidy

import sys
import mcb185

min_length = int(sys.argv[2])

with open('proteins.txt', 'w') as outfile:
	for defline, seq in mcb185.read_fasta(sys.argv[1]):
		name = defline.split()                    # split by whitespace
		for i in range(3):                        # 3 frames
			aachain = mcb185.translate(seq, i)    # translate using frame=i
			met = aachain.find('M')               # find first M
			stop = aachain.find('*', met)         # find first stop after M
			while stop - met + 1 < min_length:    # if chain is under min
				met = aachain.find('M', met + 1)  # start search from met + 1
				stop = aachain.find('*', met + 1)
			print('>', name[0], '-prot-', i, sep='', file=outfile)
			print(aachain[met:stop + 1], file=outfile)
		rc_seq = mcb185.anti_seq(seq)             # repeat on reverse comp
		for i in range(3, 6):                     # now indexing 3, 4, 5
			aachain = mcb185.translate(rc_seq, i - 3)
			met = aachain.find('M')
			stop = aachain.find('*', met)
			while stop - met + 1 < min_length:
				met = aachain.find('M', met + 1)
				stop = aachain.find('*', met + 1)
			print('>', name[0], '-prot-', i, sep='', file=outfile)
			print(aachain[met:stop + 1], file=outfile)