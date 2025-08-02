# 63kozak.py by Kassidy

import argparse
import gzip

parser = argparse.ArgumentParser(description='translation initiation')
parser.add_argument('gbff', type=str, help='gen bank flat file')
parser.add_argument('-l', '--length', type=int, default=9, 
	help='length of Kozak conesnsus before start codon')
parser.add_argument('-t', '--tail', type=int, default=2, 
	help='length of tail after start codon')
arg = parser.parse_args()

fp = gzip.open(arg.gbff, 'rt')
starts = []
anti_starts = []
# finding CDS start coordinates
while True:
	line = fp.readline().split()
	if 'ORIGIN' in line: break
	if line[0] == 'CDS':
		if 'complement' in line[1]:
			coords = line[1].lstrip('complement(')
			if 'join' in coords:
				coords = line[1].lstrip('join(')
				coords = coords.rstrip(')')
			coords = coords.rstrip(')').split('..')
			anti_starts.append(int(coords[-1]))
		else:
			if 'join' in line[1]:
				coords = line[1].lstrip('join(')
			else:
				coords = line[1]
			coords = coords.split('..')
			starts.append(int(coords[0]))

# looking through the sequence at end of file after ORIGIN
seq = []
while True:
	line = fp.readline()
	if line == '': break
	line = line.split()
	for i in range(len(line)-1): # skip the first part - number
		seq.append(line[i+1])
seq = ''.join(seq)
fp.close()

# creating empty PWM
PWM = []
for i in range(arg.length + 3 + arg.tail):
	PWM.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})

# iterate through start points and use them to add stuff to PWM
for spoint in starts:
	kstart = spoint - arg.length # start arg.length nts before start point
	kend = spoint + 2 + arg.tail # finish 2 (rest of codon) + arg.tail later
	kseq = seq[kstart-1:kend]    # find sequence of interest
	for i in range(len(kseq)):   # add to PWM as needed
		nt = kseq[i].upper()
		PWM[i][nt] += 1

# iterate through complement starts - need to complement & reverse
for spoint in anti_starts:
	kstart = spoint + arg.length      # reverse + and - since using complement
	kend = spoint - 2 - arg.tail      # rest of codon, tail
	kpos = seq[kend-1:kstart]         # using the positive strand partial seq
	comp = str.maketrans('acgt', 'tgca')
	kseq = kpos.translate(comp)[::-1] # anti_seq strategy from mcb185.py 
	for i in range(len(kseq)):
		nt = kseq[i].upper()
		PWM[i][nt] += 1

# print out the PWM formatted as given
print('AC AMU002', 'XX', 'ID ECKOZ', 'XX', 'DE Also made up', sep='\n')
title = ['PO', 'A', 'C', 'T', 'G']
for part in title:
	print(f'{part:<8}', end='')
print('')
for i in range(len(PWM)):
	a = PWM[i]['A']
	c = PWM[i]['C']
	g = PWM[i]['G']
	t = PWM[i]['T']
	print(f'{i+1:<8}', f'{a:<8}', f'{c:<8}', f'{g:<8}', f'{t:<8}')
print('XX')