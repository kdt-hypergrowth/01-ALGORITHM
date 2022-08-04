# https://www.acmicpc.net/problem/9455

import sys
sys.stdin = open('20220804/9455_박스.txt')

T = int(input())
matrix = []
distance = 0

for t in range(T):
    m, n = map(int, input().split())
    for i in range(m): # 행
        for j in range(n): # 열
            print(matrix[i][j], end=' ')




