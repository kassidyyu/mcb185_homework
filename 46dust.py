# 46dust.py by Kassidy

import sys
import mcb185
import math

window = int(sys.argv[2])
threshold = float(sys.argv[3])

output = []

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	subseq = seq[:window]
	for i in range(len(seq) - window + 1):
		a = subseq.count('A')
		c = subseq.count('C')
		g = subseq.count('G')
		t = subseq.count('T')
		n_comp = [a / window, c / window, g / window, t / window]
		entropy = 0
		for val in n_comp: # calculate the entropy each iteration
			if val == 0: continue
			entropy -= val * math.log2(val)
		if i == 0: # only for the first iteration, write in whole window
			if entropy < threshold:
				output[:window] = ['N'] * window
			else:
				for i in range(window):
					output.append(subseq[i])
		else:
			# Case 1: just add on the next nucleotide as is, no 'N's
			if entropy >= threshold:
				output.append(subseq[-1])
			# Case 2: previous iteration already has 'N's, so just add 1 'N'
			elif output[-1] == 'N' and entropy < threshold:
				output.append('N')
			# Case 3: previous iteration is above threshold, so nts are
			# written as is, but current window is below threshold.
			# Make everything in the current window 'N'
			else:
				output[i:i + window] = ['N'] * window
		if i != len(seq) - window: # indexing no longer works in last loop
			subseq = subseq[1:] + seq[i + window] # 44skew.py algorithm

	# after desired output is in list, write to new file
	with open('dust_output.txt', 'w') as outfile:
		outfile.write('>')     # defline got rid of >
		outfile.write(defline) # defline itself
		outfile.write('\n')    # separate defline from sequence
		for i in range(0, len(output) - 59, 60):     # in increments of 60
			outfile.write(''.join(output[i:i + 60]))
			outfile.write('\n')                      # line breaks
		# write in last leftover line if output is not divisible by 60
		if len(output) % 60 != 0: 
			outfile.write(''.join(output[i + 60: i + 60 + len(output) % 60]))
