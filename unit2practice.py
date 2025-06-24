# Practice Problems from Unit 2

import math
import random

# Write a function that calculates the triangular number. This is the sum of numbers from 1 to n.
def triangular(n):
	sum = 0
	for i in range(n+1):
		sum += i
	return sum

# Write a function that calculates the factorial of a number.
def factorial(n):
	product = 1
	for i in range(1, n + 1):
		product = product * i
	return product

# Write a function that computes the Poisson probability of k events occurring with an expectation of n: 
# n^k e^-n / k!
def poisson(n, k):
	return (n**k * math.e**(-n) / factorial(k))

# Write a function that solves "n choose k": n! / k!(n - k)!
def n_choose_k(n, k):
	return factorial(n) / (factorial(k) * factorial(n - k))

# Write a function that estimates Euler's number: e (2.71828...). This can be computed as the infinite sum of 1/n!. Choose a finite number of iterations.
def euler_estimate(n):
	sum = 0
	for i in range(n+1):
		sum += 1 / factorial(i)
	return sum

# Write a function to determine if a number is prime.
def is_prime(n):
	if (n == 1) or (n == 2): return True
	for i in range(2, n):
		if n % i == 0:
			return True
	return False

# Write a function that estimates Pi (3.14159...) using the Nilakantha series. Again, choose a finite limit. Pi = 3 + 4/(2x3x4) - 4/(4x5x6) + 4/(6x7x8) - 4/(8x9x10) ...
def pi_estimate(n):
	pi_sum = 3
	for i in range(n+1):
		pi_sum += (4 * (-1)**i) / ((2*i+2) * (2*i+3) * (2*i+4))
	return pi_sum

# Note: my pi_estimate function works the same except the inputted iteration is slightly different
# pi_estimate(4) is the same as nilakantha(5)

# Monty Pi-thon

"""
inside = 0
count = 0
while True:
	x = random.random()
	y = random.random()
	if math.sqrt(x**2 + y**2) < 1: inside += 1
	count += 1
	print(4 * inside / count)
"""

# D&D Stats

def three_dsix(n):
	stat_sum = 0
	for i in range(n):
		for i in range(3): stat_sum += random.randint(1, 6)
	return stat_sum / n

def three_dsix_r_one(n):
	stat_sum = 0
	for i in range(n):
		for i in range(3): stat_sum += random.randint(2, 6) # ignore 1's
	return stat_sum / n

# simulating real life rerolls
def three_dsix_r_one_alt(n):
	stat_sum = 0
	for i in range(n):
		for i in range(3):
			roll = random.randint(1, 6)
			while roll == 1:                # rerolls until you don't get 1
				roll = random.randint(1, 6) # assigns new value to same variable
			stat_sum += roll                # adds roll which will never be 1
	return stat_sum / n

def three_dsix_pairs(n):
	stat_sum = 0
	for i in range(n):
		for i in range(3):
			d1 = random.randint(1, 6)
			d2 = random.randint(1, 6)
			if d1 >= d2: stat_sum += d1
			else:        stat_sum += d2
	return stat_sum / n

def four_dsix_drop_one(n):
	stat_sum = 0
	for i in range(n):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		d3 = random.randint(1, 6)
		d4 = random.randint(1, 6)
		if   d1 <= d2 and d1 <= d3 and d1 <= d4: stat_sum += d2 + d3 + d4
		elif d2 <= d1 and d2 <= d3 and d2 <= d4: stat_sum += d1 + d3 + d4
		elif d3 <= d1 and d3 <= d2 and d3 <= d4: stat_sum += d1 + d2 + d4
		else:                                    stat_sum += d1 + d2 + d3
	return stat_sum / n