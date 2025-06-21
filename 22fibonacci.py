# 22fibonacci.py by Kassidy

def fibonacci(n):
    start = 0
    next = 1
    print(start)
    print(next)
    for i in range(n-2):        # n-2 since we start with 0 and 1
        print(start + next)
        old_start = start       # this allows the next reassignment to work
        start = next            # start goes up one index
        next = old_start + next # uses the old value of start

fibonacci(10)