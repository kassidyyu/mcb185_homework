import argparse
import itertools

parser = argparse.ArgumentParser()
parser.add_argument('pins', type=int, help='number of pins')
parser.add_argument('cuts', type=int, help='number of cuts')
parser.add_argument('--heights', type=int, default=3,
	help='number of different heights [%(default)i]')
parser.add_argument('--maxdiff', type=int, default=5,
	help='maximum height difference between pins [%(default)i]')
parser.add_argument('--verbose', action='store_true')
arg = parser.parse_args()

count = 0
for key in itertools.product(range(arg.cuts), repeat=arg.pins):
	# check heights, make sure there are enough different heights
	sizes = set(key)
	if len(sizes) < arg.heights: continue

	# check for stuck keys (adjacent max diff too big)
	stuckkey = False
	for i in range(1, len(key)):
		if abs(key[i-1] - key[i]) > arg.maxdiff:
			stuckkey = True
			break
	if stuckkey: continue 

	# save or print
	if arg.verbose: print(key)
	count += 1

print(count)