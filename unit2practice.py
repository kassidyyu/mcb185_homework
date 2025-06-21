# Practice Problems from Unit 2

import math

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
