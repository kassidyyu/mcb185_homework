# 32stats.py by Kassidy

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

# print the results with rounding
print('There are', vals_count, 'values')
print('The minimum is', minimum, 'and the maximum is', maximum)
print(f'The mean is {mean:.2f}')
print(f'The standard deviation is {sd:.2f}')
print('The median is', median)