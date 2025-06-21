# 21fizzbuzz.py

for i in range(1, 101):
    if i % 3 == 0: print('Fizz', end='')       # end='' to allow for FizzBuzz
    if i % 5 == 0: print('Buzz', end='')
    if (i % 3 != 0) and (i % 5 != 0): print(i) # multiple of neither 3 nor 5
    else: print('') # prints a newline for Fizz, Buzz, or FizzBuzz   