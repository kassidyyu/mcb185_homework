# 54missingkmers.py

import sys
import mcb185
import itertools

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	missing_kmer = False        # initialize boolean
	missing_list = []           # keep track of missing kmers
	anti = mcb185.anti_seq(seq) # check other strand too
	k = 1                       # start with k = 1
	while not missing_kmer:     # loop until missing kmers
		for nts in itertools.product('ATCG', repeat=k):
			kmer = ''.join(nts)
			# check for each kmer in both strands
			if kmer not in seq and kmer not in anti:
				missing_list.append(kmer) # keep track of kmers
				missing_kmer = True       # update to true, no need to cont
		k += 1                  # keep iterating 

# report the list of missing kmers
print(missing_list)