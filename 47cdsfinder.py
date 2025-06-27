# 47cdsfinder.py by Kassidy

import sys
import mcb185

min_length = int(sys.argv[2]) #

with open('proteins.txt', 'w') as outfile:
	for defline, seq in mcb185.read_fasta(sys.argv[1]):
		name = defline.split()                    # split by whitespace
		name = '>' + name[0] + '-prot-'           # format naming as shown
		for i in range(3):                        # 3 frames
			aachain = mcb185.translate(seq, i)    # translate using frame=i
			met = aachain.find('M')               # find first M
			stop = aachain.find('*', met)         # find first stop after M
			while stop - met + 1 < min_length:    # if chain is under min
				met = aachain.find('M', met + 1)  # start search from met + 1
				stop = aachain.find('*', met + 1)
			outfile.write(name)                   # writes >NC_000913.3-prot-
			outfile.write(str(i))                 # adds which orf
			outfile.write('\n')                   # newline for chain
			outfile.write(aachain[met:stop + 1])  # chain at least min_length
			outfile.write('\n')                   # newline for next chain
		rc_seq = mcb185.anti_seq(seq)             # repeat on reverse comp
		for i in range(3, 6):                     # now indexing 3, 4, 5
			aachain = mcb185.translate(rc_seq, i - 3)
			met = aachain.find('M')
			stop = aachain.find('*', met)
			while stop - met + 1 < min_length:
				met = aachain.find('M', met + 1)
				stop = aachain.find('*', met + 1)
			outfile.write(name)
			outfile.write(str(i))
			outfile.write('\n')
			outfile.write(aachain[met:stop + 1])
			outfile.write('\n')