# 33birthday.py by Kassidy

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

success = 0
for i in range(trials):
    birthday_list = []
    for person in range(people):
        birthday = random.randint(1, days) # assign a random birthday
        if birthday not in birthday_list:  # only append if not duplicate
            birthday_list.append(birthday)
        else:                              # otherwise, duplicate
            success += 1                   # matching birhtdays
            break                          # no need to continue for loop
print(success / trials) # simulated probability of matching birhtdays