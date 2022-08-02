# https://www.acmicpc.net/problem/14720

import sys
sys.stdin = open('20220801/14720_우유축제.txt')

T = int(input())

for t in range(T):
    milk = list(map(int, input().split()))
    cnt = 0

    for m in milk:
        if milk[m] == 0 and milk[m-1] == 2:
            cnt += 1
        elif milk[m] == 1 and milk[m-1] == 0:
            cnt += 1
        elif milk[m] == 2 and milk[m-1] == 1:
            cnt += 1
    print(cnt)


