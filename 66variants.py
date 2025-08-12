# 66variants.py by Kassidy (updated version in progress)

import argparse
import gzip

parser = argparse.ArgumentParser(description='variant reporter')
parser.add_argument('gff', type=str, help='GFF file')
parser.add_argument('vcf', type=str, help='VCF file')
arg = parser.parse_args()

# read through the vcf file and create a catalog with variant coordinates
fp = gzip.open(arg.vcf, 'rt')
vars = []
while True:
	line = fp.readline()
	if line == '': break
	line = line.split()
	# would be altered if vcf were ranges, depends on how it is noted
	loc = int(line[1])
	# use increments of 10,000 as the 'zipcode' to check against later
	vrec = {'chr': line[0], 'loc': loc, 'sec': loc // 10000}
	vars.append(vrec)

# make a catalog of the relevant info - name, start, & end coordinates
fcat = []
fp = gzip.open(arg.gff, 'rt')
while True:
	line = fp.readline()
	if line == '': break
	line = line.split()
	# finding 'zipcodes'
	frec = {'chr': line[0], 'feat': line[2], 'beg': int(line[3]), 'end': int(line[4])}
	fcat.append(frec)

# iterate through the variants
for vrec in vars:
	# create a feature list
	feats = []
	for frec in fcat:
		# first, only compare when same chromosome
		if frec['chr'] != vrec['chr']: continue
		# check the 'zipcode'
		if frec['beg'] // 10000 != vrec['sec'] and frec['end'] // 10000 != vrec['sec']: continue
		# different if statement here if the variants are ranges
		if vrec['loc'] >= frec['beg'] and vrec['loc'] <= frec['end']:
			if frec['feat'] not in feats: 
				feats.append(frec['feat'])
	# prints feature list if non-empty
	if feats: print(vrec['chr'], vrec['loc'], ','.join(feats), sep='\t')