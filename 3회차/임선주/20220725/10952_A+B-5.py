# https://www.acmicpc.net/problem/10952

import sys
sys.stdin = open('20220725/10952_A+B-5.txt')

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a + b)