# 24savingthrows.py by Kassidy

import random

def saving_throw(dc, n): # enter DC, number of trials
    success = 0
    success_adv = 0
    success_dis = 0
    for i in range(n):
        roll1 = random.randint(1, 20)
        roll2 = random.randint(1, 20)
        if roll1 >= dc:                 success += 1
        if roll1 >= dc or roll2 >= dc:  success_adv += 1
        if roll1 >= dc and roll2 >= dc: success_dis += 1 
    return success / n, success_adv / n, success_dis / n

print(saving_throw(5, 1000))  # DC of 5
print(saving_throw(10, 1000)) # DC of 10
print(saving_throw(15, 1000)) # DC of 15