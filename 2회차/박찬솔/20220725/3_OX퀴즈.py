# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input())

for i in range(T):
    a = list(input())
    cnt = 0
    sum = 0
    for i in a:
        if i == 'O':
            cnt += 1
            sum = sum+cnt
        else:
            cnt = 0
    print(sum)