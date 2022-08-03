# https://www.acmicpc.net/problem/10871

import sys
sys.stdin = open('20220725/10871_X보다작은수.txt')

N, X = map(int, input().split())
numbers = list(map(int, input().split()))

for n in numbers:
    if n < X:
        print(n, end=' ')
