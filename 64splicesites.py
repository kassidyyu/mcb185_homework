# 64splicesites.py by Kassidy

import argparse
import gzip
import mcb185

parser = argparse.ArgumentParser(description='splice sites')
parser.add_argument('fasta', type=str, help='FASTA file')
parser.add_argument('gff', type=str, help='GFF file')
parser.add_argument('-a', '--acceptor', type=int, default=7, 
	help='length of acceptor sequence')
parser.add_argument('-d', '--donor', type=int, default=6,
	help='length of donor sequence')
arg = parser.parse_args()

# initialize PWMs
acceptor_PWM = []
for i in range(arg.acceptor):
	acceptor_PWM.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})

donor_PWM = []
for i in range(arg.donor):
	donor_PWM.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})

# save all introns with chromosome, start, & stop
fp = gzip.open(arg.gff, 'rt')
sites = []
while True:
	line = fp.readline()
	if line == '': break
	line = line.split()
	if line[2] == 'intron':
		irec = {'chr': line[0], 'beg': int(line[3]), 'end': int(line[4])}
		sites.append(irec)
fp.close()

# read through all chromosomes and sequences
seqcat = []
for defline, seq in mcb185.read_fasta(arg.fasta):
	defline = defline.split()
	chr = defline[0]
	crec = {'chr': chr, 'seq': seq}
	seqcat.append(crec)

for irec in sites:
	# find the chromosome in question and extract its sequence
	for crec in seqcat:
		if crec['chr'] == irec['chr']:
			chrseq = crec['seq']
	# find the donor sequence (starts at coordinate-1 index), up to arg.donor length more
	dseq = chrseq[irec['beg'] -1 : irec['beg'] -1 +arg.donor]
	# find acceptor sequence (end - arg.acceptor up to end)
	aseq = chrseq[irec['end'] -arg.acceptor : irec['end']]
	# add values to the PWMs
	for i in range(len(dseq)):
		nt = dseq[i]
		donor_PWM[i][nt] += 1
	for i in range(len(aseq)):
		nt = aseq[i]
		acceptor_PWM[i][nt] += 1

# print out the PWM formatted as given
print('AC MU01', 'XX', 'ID ACC', 'XX', 'DE splice acceptor', sep='\n')
title = ['PO', 'A', 'C', 'T', 'G']
for part in title:
	print(f'{part:<8}', end='')
print('')
for i in range(len(acceptor_PWM)):
	a = acceptor_PWM[i]['A']
	c = acceptor_PWM[i]['C']
	g = acceptor_PWM[i]['G']
	t = acceptor_PWM[i]['T']
	print(f'{i+1:<8}', f'{a:<8}', f'{c:<8}', f'{g:<8}', f'{t:<8}')
print('XX', '//', sep='\n')
# donor PWM
print('AC MU02', 'XX', 'ID DON', 'XX', 'DE splice donor', sep='\n')
for part in title:
	print(f'{part:<8}', end='')
print('')
for i in range(len(donor_PWM)):
	a = donor_PWM[i]['A']
	c = donor_PWM[i]['C']
	g = donor_PWM[i]['G']
	t = donor_PWM[i]['T']
	print(f'{i+1:<8}', f'{a:<8}', f'{c:<8}', f'{g:<8}', f'{t:<8}')
print('XX', '//', sep='\n')

# note: slightly different numbers - indexing issue?