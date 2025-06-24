# 25deathsaves.py by Kassidy

import random

def death_saves(n):   # given some large number of trials
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

print(death_saves(1000))