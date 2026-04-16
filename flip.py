import random

n = int(input("Enter number of coin flips: "))

if n <= 0:
    print("Enter a positive integer!")
else:
    heads = 0
    tails = 0

    for _ in range(n):
        if random.random() < 0.5:
            tails += 1
        else:
            heads += 1

    print("Heads %:", (heads / n) * 100)
    print("Tails %:", (tails / n) * 100)
