# 25deathsaves.py by Kassidy

import random

def death_saves(n):
    death_count = 0
    stable_count = 0
    revived_count = 0
    for i in range(n):
        failures = 0
        successes = 0
        dead = False
        stable = False
        revived = False
        while not dead and not stable and not revived:                
            roll = random.randint(1, 20)
            if roll == 20:
                revived = True
                revived_count += 1
            elif roll == 1: failures += 2
            elif roll < 10: failures += 1
            else: successes += 1
            if failures == 3:
                dead == True
                death_count += 1
            if successes == 3:
                stable = True
                stable_count += 1
    return death_count / n, stable_count / n, revived_count / n

print(death_saves(1000))