# 61prosite.py by Kassidy

import sys
import mcb185
import re

# find pattern "D-K-T-G-T"
"""
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if 'DKTGT' in seq: print(defline)
	
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if re.search('DKTGT', seq): print(defline) # pattern, string
"""

# same syntax as grep, find "D-K-T-G-T-[LIVM]-[TI]"
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if re.search('DKTGT[LIVM][TI]', seq): print(defline)

# "C-x(2,4)-C-x(3)-[LIVMFYWC]-x(8)-H-x(3,5)-H"
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if re.search('C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H', seq): print(defline)

pat = '(C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H)' # abstracts pattern into variable
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	m = re.search(pat, seq) # assign search to a variable
	if m: print(m.group(1)) # retrieves matched string if it has a value