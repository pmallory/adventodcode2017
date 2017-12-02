import itertools
import sys

s = sys.stdin.readlines()

total = 0

for line in s:
    l = [int(n) for n in line.split()]
    for a, b in itertools.permutations(l, 2):
        a, b = max(a,b), min(a,b)
        if a % b == 0:
            total += a/b
            break

print(total)
