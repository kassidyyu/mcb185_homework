# Lab Meeting Discussion 8/18

import random

genome_size = 50000
read_size = 5
coverage = 4
# rule 1 - work with a tiny data set!
# low coverage - huge differences in numbers
# high coverage - very stable in the middle but the ends become much smaller
# why is it bad at the end, how many positions are bad? 9 positions? when read length is 10
# number of bad positions = 1 less than the read length - in order for end position to be hit, need to hit exactly there

reads = coverage * genome_size // read_size

genome = [0] * genome_size
for _ in range(reads):
	ipos = random.randint(0, genome_size - read_size)
	for i in range(ipos, ipos+read_size): genome[i] += 1

#print(genome)

maxd = 25
depth = [0] * maxd
for x in genome[read_size:-read_size]: 
	if x >= maxd: continue
	depth[x] += 1
# don't start at 0 start in a bit, can't use undersampled
for n, x in enumerate(depth):
	print(n, x/(genome_size))

# read size doesn't matter! genome size doesn't matter! only coverage
# poisson distribution - random sampling of the genome
# if you roll a 100 sided die 100 times do you hit every number? no
# 400 times - on average, 2 spots will be 0

# how many reads do you need in order to determine heterozygous or homozygous?
# need to hit every part of the genome and hit with a lot of reads

# A/G
# 40x
# 40 A -> hom
# ....
# 35 A 5 G --> 1 in a mill times
# ....
# 20 A 20 G --> heterozygous
# becomes an alignment problem - a counting problem
# do 50x 