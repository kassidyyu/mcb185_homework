# 66variants.py by Kassidy

import argparse
import gzip

parser = argparse.ArgumentParser(description='variant reporter')
parser.add_argument('gff', type=str, help='GFF file')
parser.add_argument('vcf', type=str, help='VCF file')
arg = parser.parse_args()

# read through the vcf file and create a list of all variant coordinates
fp = gzip.open(arg.vcf, 'rt')
vars = []
while True:
	line = fp.readline()
	if line == '': break
	line = line.split()
	vars.append([line[0], int(line[1])])

# make a catalog of the relevant info - name, start, & end coordinates
fcat = []
fp = gzip.open(arg.gff, 'rt')
while True:
	line = fp.readline()
	if line == '': break
	line = line.split()
	frec = {'feat': line[2], 'beg': int(line[3]), 'end': int(line[4])}
	fcat.append(frec)

# sort by the beginning indices to catch all features
fcat.sort(key=lambda d: d['beg'])

# pointer for the fcat
f_point = 0
for var in vars:
	# initialize/reset list of features and boolean variables
	feats = []
	found = False
	start = False
	while not found:
		if var[1] <= fcat[f_point]['end'] and not start:
			while not start:
				if f_point == 0: # no more decrementing, start at 0
					start = True # exit this loop
				# keep decrementing f_point until var > end point		
				elif var[1] <= fcat[f_point]['end']:
					f_point -= 1
				# add back 1 so we have first potential range for var
				else: 
					start = True
					f_point += 1
		# feature range is before the variant, increment pointer
		elif var[1] > fcat[f_point]['end']:
			start = True
			f_point += 1
		# when the variant is in the range of the feature
		elif var[1] >= fcat[f_point]['beg'] and var[1] <= fcat[f_point]['end']:
			start = True 
			# if statement prevents duplicates (e.g. intron,intron,intron)
			if fcat[f_point]['feat'] not in feats:
				feats.append(fcat[f_point]['feat'])
			f_point += 1
		else: # start = True and var < beg so everything is found
			found = True
	# only print output if feats list is nonempty
	if feats: print(var[0], var[1], ','.join(feats), sep='\t')
