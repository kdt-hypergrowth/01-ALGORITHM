# https://www.acmicpc.net/problem/5533

import sys
sys.stdin = open('20220803/5533_유니크.txt')

from pprint import pprint

N = int(input())
number = [[], [], []]
score = []

for _ in range(N):
    a, b, c = map(int, input().split())
    number[0].append(a)
    number[1].append(b)
    number[2].append(c)

        # 같은 수가 2개 이상이면 0점

        # 같은 수가 없으면 점수 획득





