# 55genefinder.py by Kassidy

import argparse
import mcb185

parser = argparse.ArgumentParser(description='Putative coding gene finder')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-l', '--length', type=int, default=300, 
	help='minimum ORF length [%(default)i]')
arg = parser.parse_args()

def make_lists(seq, frame, forward=True):
	if forward: adj = 1
	else:       adj = 0
	start_pos = []
	stop_pos = []
	frame = int(frame)
	for i in range(frame, len(seq), 3):
		if seq[i:i+3] == 'ATG':
			start_pos.append(i+adj)
		elif seq[i:i+3] == 'TAA' or seq[i:i+3] == 'TAG' or seq[i:i+3] == 'TGA':
			stop_pos.append(i+adj+2)
	return(start_pos, stop_pos)

def find_cds(start_pos, stop_pos, length, out_list):
	met_point = 0
	end_point = 0
	while met_point < len(start_pos) and end_point < len(stop_pos):
		if start_pos[met_point] > stop_pos[end_point]:
			end_point += 1
		else:
			if stop_pos[end_point] - start_pos[met_point] >= length:
				out_list.append((start_pos[met_point], stop_pos[end_point]))
			met_point += 1
	return out_list


for defline, seq in mcb185.read_fasta(arg.file):
	name = defline.split()
	out_list = []
	# first reading frame
	start_pos, stop_pos = make_lists(seq, 0)
	out_list = find_cds(start_pos, stop_pos, arg.length, out_list)

	# second reading frame
	start_pos, stop_pos = make_lists(seq, 1)
	out_list = find_cds(start_pos, stop_pos, arg.length, out_list)

	# third reading frame
	start_pos, stop_pos = make_lists(seq, 2)
	out_list = find_cds(start_pos, stop_pos, arg.length, out_list)

	# reverse strand
	minus = mcb185.anti_seq(seq)
	minus_list = []
	start_pos, stop_pos = make_lists(minus, 0, False)
	minus_list = find_cds(start_pos, stop_pos, arg.length, minus_list)

	# second minus frame
	start_pos, stop_pos = make_lists(minus, 1, False)
	met_point = 0
	end_point = 0
	minus_list = find_cds(start_pos, stop_pos, arg.length, minus_list)

	# third minus frame
	start_pos, stop_pos = make_lists(minus, 2, False)
	minus_list = find_cds(start_pos, stop_pos, arg.length, minus_list)
	
	with open('ecoli_cds.gff', 'w') as outfile:
		print('#cdsfinder-mock-gff', file=outfile)
		i = 1
		for crd in out_list:
			print('NC_000913.3\tRefSeq\tCDS', crd[0], crd[1], sep='\t', end='\t', file=outfile)
			print('.\t+\t0\tID=cds-plus-no.', i, sep='', file=outfile)
			i += 1
		j = 1
		for crd in minus_list:
			print('NC_000913.3\tRefSeq\tCDS', crd[0], crd[1], sep='\t', end='\t', file=outfile)
			print('.\t-\t0\tID=cds-minus-no.', j, sep='', file=outfile)
			j += 1
