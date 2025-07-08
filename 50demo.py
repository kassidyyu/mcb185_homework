# 50demo.py by Kassidy

"""s = {'A', 'C', 'G'}
print(s)

s.add('T')
print(s)

s.add('A')
print(s)"""

d = {'dog': 'woof', 'cat': 'meow'}
print(d)
print(d['cat'])

d['pig'] = 'oink'
print(d)

d['cat'] = 'mew'
print(d)

del d['cat']
print(d)
# print(d['rat'])

if 'dog' in d: print(d['dog'])

for key in d: print(f'{key} says {d[key]}')

for k, v in d.items(): print(k, 'says', v)

# for thing in d.items(): print(thing[0], thing[1])

print(d.keys(), d.values(), list(d.values()))