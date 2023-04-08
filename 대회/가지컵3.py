import sys
from itertools import product

input = sys.stdin.readline

candidates = set(product([1,0], repeat=11))

for i in range(2047):
    candidate = tuple(map(int, input().strip().split()))
    candidates.remove(candidate)
    
for i in candidates[0]:
    print(str(i), end = " ")