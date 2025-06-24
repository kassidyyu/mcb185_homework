# 20demo.py by Kassidy

import random

# while True:
#   print('hello')

for i in range(5): print(i)
for i in range(4, -1, -1): print(i)

basket = 'milk', 'eggs', 'bread'
for thing in basket:
	print(thing)

for i in range(len(basket)):
	print(basket[i])

for i in range(7):
	if i % 2 == 0: print(i, 'is even')
	else:          print(i, 'is odd')

for i in range(5):
	print(random.random())

for i in range(3):
	print(random.randint(1, 6))

random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())