import sys
import random

n = random.randint(1, 10)
print(n)

while True:
    v = sys.stdin.readline()
    print("HEllo " + v)

    i = int(v)
    if i == n:
        print("guessed right")
        break
    elif i > n:
        print("number is smaller")
    elif i < n:
        print("number is greater")
    
    