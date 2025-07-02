# Unit 4 Assessment by Kassidy

import sys
import math
import random
import mcb185

# 1. Statistical summary of length of sequences in FASTA file
s_lens = []
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	s_lens.append(len(seq))

s_lens.sort()
if len(s_lens) % 2 == 0: # calculation depends on if vals_count is even or odd
	median = (s_lens[int(len(s_lens)/2)] + s_lens[int(len(s_lens)/2 - 1)]) / 2
else: median = s_lens[int(math.floor(len(s_lens) / 2))] 

sum = 0
for n in s_lens: sum += n
mean = sum / len(s_lens)

sd_sum = 0
for n in s_lens: sd_sum += (n - mean)**2 # sum the differences squared
sd = math.sqrt(sd_sum / len(s_lens))    # standard deviation formula

# N50 calculation
contig_sum = 0
for i in range(len(s_lens) - 1, -1, -1): # iterate backwards through list
	contig_sum += s_lens[i]
	if contig_sum >= sum / 2:
		n50 = s_lens[i]
		break

print('There are', len(s_lens), 'sequences')
print('The minimum length is', s_lens[0], 'and the maximum is', s_lens[-1])
print(f'The mean length is {mean:.2f}')
print(f'The standard deviation is {sd:.2f}')
print('The median length is', median)
print('The N50 is', n50)

# 2. Write a program that generates random FASTA files. 
# The names should be unique and the sequences should be random.
upper_alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
random_char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890.-+: '
def random_fasta(num_seq):
	name = random.choices(upper_alph, k = 2)
	name.append('_')
	for i in range(num_seq):
		seq_name = name
		for j in range(6):
			seq_name.append(random.randint(0, 9))
		seq_name.append('.')
		seq_name.append(random.randint())
		seq_name.append(random.choices(random_char, k = random.randint()))
		''.join(seq_name)
		print('>', seq_name, sep='')
		print(random.choices(upper_alph, k = random.randint()))

# 3. Modify program 42 to also report the average over all sequences.
nts = [] # keep a running list of nts
total_counts = [] # grand total counts
sum_seq_len = 0
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	sum_seq_len += len(seq)
	defwords = defline.split()
	name = defwords[0]
	counts = [] # reset counts for specific seq
	for nt in seq:
		if nt not in nts:
			nts.append(nt)
			counts.append(0)
			total_counts.append(0)
		idx = nts.index(nt)
		counts[idx] += 1
		total_counts[idx] += 1
	print(name)
	for nt, n in zip(nts, counts):
		print(nt, n, n/len(seq))

for nt, n in zip(nts, total_counts):
	print('The average composition of', nt, 'over all sequances is', n/sum_seq_len)

# 4. I would make separate functions of each distance measure of interest.
# I would find the corresponding closest distance for any given RGB values
# then compare the resulting colors to each other to find any differences.