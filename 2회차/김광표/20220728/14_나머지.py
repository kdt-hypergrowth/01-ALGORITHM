# 3052 나머지 B2

import sys

sys.stdin = open("14_나머지.txt")

N = []
for i in range(10) :
    n = int(input())
    N.append(n%42)
N = list(set(N))

print(len(N))