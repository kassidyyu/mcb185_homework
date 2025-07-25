# 62transfac.py by Kassidy

import gzip
import sys
import json

outputlist = []
fp = gzip.open(sys.argv[1], 'rt')

while True:
	line = fp.readline()
	if line == '': break
	line = line.split()
	if line[0] == 'ID':
		d = {}
		d['id'] = line[1]
	if line[0] == 'PO': # start of pwm
		matrix = False  # finished matrix
		acgt = {}       # empty dict for nts
		pwm_list = []   # list for the pwm
		while not matrix:
			pwmline = fp.readline()      # read rows of pwm
			if pwmline.startswith('XX'): # end of pwm 
				matrix = True            # end the loop
				d['pwm'] = pwm_list
				outputlist.append(d)
			else:
				pwmline = pwmline.split()
				acgt['A'] = float(pwmline[1])
				acgt['C'] = float(pwmline[2])
				acgt['G'] = float(pwmline[3])
				acgt['T'] = float(pwmline[4])
				# append row dict then reset
				pwm_list.append(acgt)
				acgt = {}

# print output list in json format
print(json.dumps(outputlist, indent=4))	
