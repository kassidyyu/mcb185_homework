# 60demo.py by Kassidy

import sys
import dogma

print(sys.argv)
print(sys.argv[0])
print(sys.argv[0][3])

d = [
	'hello',
	(3.14, 'pi'),
	[-1, 0, 1],
	{'year': 2000, 'month': 7}
]
print(d[0][4], d[1][0], d[2][2], d[3]['month'])

# record: data type with various named fields
oligo = {
	'Name': 'SO116',
	'Length': 18,
	'Sequence': 'ATTTAGGTGACACTATAG',
	'Description': 'SP6 promoter sequencing primer'
}

# catalog: list of records
catalog = []
catalog.append(oligo)

def read_catalog(filepath):
	catalog = []
	with open(filepath) as fp:
		for line in fp:
			if line.startswith('#'): continue
			name, length, seq, desc = line.rstrip().split(',')
			record = {
				'Name': name,
				'Length': length,
				'Sequence': seq,
				'Description': desc
			}
			catalog.append(record)
	return catalog

catalog = read_catalog('primers.csv')
for primer in catalog:
	print(primer['Name'], primer['Description'])

# adding melting temperature for each oligo
for primer in catalog:
	primer['Tm'] = dogma.tm(primer['Sequence'])
print(catalog)

# saving locations of kmers
seq = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGT'
k = 2
kloc = {}
for i in range(len(seq) -k +1):
	kmer = seq[i:i+k]
	if kmer not in kloc: kloc[kmer] = []
	kloc[kmer].append(i)
print(kloc)

# JSON: Javascript Object Notation
import json

truc = {
	'animals': {'dog': 'woof', 'cat': 'meow', 'pig': 'oink'},
	'numbers': [1.09, 2.72, 3.14],
	'is_complete': False,
}
print(json.dumps(truc, indent=4)) # change format to JSON