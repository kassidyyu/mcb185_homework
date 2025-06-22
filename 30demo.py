# 30demo.py by Kassidy

import math
import sys
print(sys.argv)

"""
s = 'hello world'
print(s)

s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)

print('hey "dude" don\'t tell me what to do')

print(s.upper())
print(s)

print(s.replace('o', '')) # removes o
print(s.replace('o', '').replace('r', 'i')) # removes o and replaces r with i
print(s) # s is still the same

print(f'{math.pi}')
print(f'{math.pi:.3f}')
print(f'{1e6 * math.pi:e}')
print(f'{"hello world":>20}')
print(f'{"hello world":.>20}')
print(f'{20:<10} {10}')

print('{} {:.3f}'.format('str.format', math.pi))

print('%s %.3f' % ('printf', math.pi))

seq = 'GAATTC'

for nt in seq:
    print(nt, end='')
print()

for i in range(len(seq)):
    print(i, seq[i])

print(seq[:4])

s = 'ABCDEFGHIJ'
print(s, s[::], s[::1], s[::-1])
print(s[::2])

tax = ('Homo', 'sapiens', 9606)
print(tax[::-1])

nts = 'ACGT'
for i, nt in enumerate(nts):
    print(i, nt)

names = ('adenine', 'cytosine', 'guanine', 'thymine')
for nt, name in zip(nts, names):
    print(nt, name)

for i, (nt, name) in enumerate(zip(nts, names)):
    print(i, nt, name)

nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

nts.append('C')
print(nts)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)
"""

items = list()
print(items)
items.append('eggs')
print(items)

stuff = []
stuff.append(3)
print(stuff)

alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
aas = list(alph)
print(aas)

text = 'good day           to you'
words = text.split()
print(words)

line = '1.41,2.72,3.14'
print(line.split(','))

s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

print('index G?', alph.index('G'))
print('index Z?', alph.index('Z'))

print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))
print('find a?', alph.find('a'))

# x = float('hello')