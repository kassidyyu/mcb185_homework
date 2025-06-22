# Unit 2 Assessment by Kassidy

import random

# 1. My fizzbuzz.py was already efficient as I could make it.
for i in range(1, 101):
    if i % 3 == 0: print('Fizz', end='')       # end='' to allow for FizzBuzz
    if i % 5 == 0: print('Buzz', end='')
    if (i % 3 != 0) and (i % 5 != 0): print(i) # multiple of neither 3 nor 5
    else: print('') # prints a newline for Fizz, Buzz, or FizzBuzz

# 2. Gregory-Leibniz pi estimate
"""
pi_fourths = 1
i = 1
while True: # endless iterations
    i += 1
    pi_fourths += (-1)**i * (1 / (2 * i + 1))
    print(4 * pi_fourths)
"""
# 3. Modified death_saves
def halflings_death_saves(n):   # given some large number of trials
    death_count = 0   # initializing counts
    stable_count = 0
    revived_count = 0 
    for i in range(n):
        failures = 0  # reset failure and success count
        successes = 0
        dead = False  # reset dead/stable/revived status
        stable = False
        revived = False
        # continue to roll until reaching death, stability, or revival
        while not dead and not stable and not revived: 
            roll = random.randint(1, 20)
            roll2 = random.randint(1, 20)
            if roll2 > roll: roll = roll2   # sets roll as larger value
            if roll == 20:                  
                revived = True              # rest of block does not run
                revived_count += 1          # conclusion (revival) reached
            elif roll == 1: failures += 2
            elif roll < 10: failures += 1   # not necessary to exclude 1
            else:           successes += 1  # only runs for rolls 10 to 19
            if failures == 3:               # checks if count has reached 3
                dead == True                # conclusion (death) reached
                death_count += 1
            if successes == 3:              # same for successes
                stable = True
                stable_count += 1
    # returns the probability of dying, stabilizing, and reviving
    return death_count / n, stable_count / n, revived_count / n

"""
4. For both of these, I would define a function that requires an input of
number of iterations or precision respectively.
(a) I would change the while loop to a for loop with n iterations
and return the result after the for loop completes.
(b) I would check the difference between the estimate and math.pi and 
compare it against the given precision with a line as follows
if abs(4 * pi_fourths - math.pi) <= precision: return 4 * pi_fourths
"""