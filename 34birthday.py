# 34birthday.py by Kassidy

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])


success = 0
for n in range(trials):
    calendar = []
    # calendar starts as a list of 0's with length = days
    for i in range(days): calendar.append(0)
    for person in range(people):
        birthday = random.randint(0, days - 1) # due to python indexing
        calendar[birthday] += 1
        if calendar[birthday] == 2:            # indicates matching bithday
            success += 1                       # success
            break                              # no need to continue loop
print(success / trials) # simulated probability of success