# Unit 3 Assessment by Kassidy

# 1. This would print out -C-. Since the parentheses close before [3:6],
# the joining of the list happens first. Then, index 3, 4, and 5 are printed.

# 2. Add N50 to 32stats.py
import sys
import math

nums = []
for arg in sys.argv[1:]:
	nums.append(float(arg))

vals_count = len(nums)

nums.sort()             # necessary for finding median
minimum = nums[0]       # can use indices since list is sorted
maximum = nums[-1]
if vals_count % 2 == 0: # calculation depends on if vals_count is even or odd
	median = (nums[int(vals_count / 2)] + nums[int(vals_count / 2 - 1)]) / 2
else: median = nums[int(math.floor(vals_count / 2))] 

sum = 0
for n in nums: sum += n # sum all values
mean = sum / vals_count

sd_sum = 0
for n in nums: sd_sum += (n - mean)**2 # sum the differences squared
sd = math.sqrt(sd_sum / vals_count)    # standard deviation formula

# N50 calculation
contig_sum = 0
for i in range(len(nums) - 1, -1, -1): # iterate backwards through list
	contig_sum += nums[i]
	if contig_sum >= sum / 2:
		n50 = nums[i]
		break

# print the results with rounding
print('There are', vals_count, 'values')
print('The minimum is', minimum, 'and the maximum is', maximum)
print(f'The mean is {mean:.2f}')
print(f'The standard deviation is {sd:.2f}')
print('The median is', median)
print('The N50 is', n50)

# 3. Position, frame, and codon separated by tabs
def codons(nts):
	nts = list(nts)
	# need length - 2 to stop at last codon
	for i in range(len(nts) - 2):
		frame = (i + 1) % 3
		if frame == 0: frame = 3 # re-assigns frame to display 3 not 0
		print(i + 1, frame, sep='\t', end='\t')
		print(nts[i], nts[i + 1], nts[i + 2], sep='')
		# use i + 1 since i starts at 0, % 3 gives frame

# 4. The strategy for 33 feels more intuitive. I think the strategy for 34 
# would be more useful in cases where we care more multiple matches. The 
# strategy for 33 with short circuiting seems more useful we want to stop as 
# soon as there is a match.