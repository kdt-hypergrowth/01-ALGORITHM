# https://www.acmicpc.net/problem/5063

import sys
sys.stdin = open('20220802/5063_TGN.txt')

T = int(input())

for t in range(T):
    r, e, c = list(map(int, input().split()))
    if r > e - c:
        print('do not advertise')
    elif r < e - c:
        print('advertise')
    else:
        print('does not matter')



