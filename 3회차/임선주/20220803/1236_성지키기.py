# https://www.acmicpc.net/problem/1236

import sys
sys.stdin = open('20220803/1236_성지키기.txt')

from pprint import pprint

# 비어있는 행 또는 열 중에 큰 값만 만족시키면 나머지는 저절로 충족되는데 이걸 어케하지

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

pprint(matrix)

