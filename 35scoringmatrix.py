# 35scoringmatrix.py by Kassidy

import sys

nts = sys.argv[1]
match = sys.argv[2]
mismatch = sys.argv[3]

nt_list = [' ']           # start list with empty space for aligning text
for char in nts:
    nt_list.append(char)  # add characters individually

for char in nt_list:
    print(char, end='  ') # prints first row with extra space for alignment
print('')                 # newline after first row

for i, nt in enumerate(nts):
    print(nts[i], end=' ')                  # row titles
    for j in range(len(nt_list)-1):         # iterate through nts
        if i == j: print(match, end=' ')    # prints match value
        else:      print(mismatch, end=' ') # prints mismatch value
    print('')                               # newline after each row