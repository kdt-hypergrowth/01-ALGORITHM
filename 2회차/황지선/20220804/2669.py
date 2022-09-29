# 2669번 직사각형 네개의 합집합의 면적 구하기

import sys

board = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split(" "))
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = 1

count = 0
for row in board:
    count += sum(row)

print(count)