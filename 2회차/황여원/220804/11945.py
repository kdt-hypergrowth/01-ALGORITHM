# n, m = map(int, input().split())

# for _ in range(n) :
#   data = input()
#   print(data[::-1])
import sys

N, M = map(int, sys.stdin.readline().split())
matrix = [list(input()) for _ in range(N)]
# [['0', '0', '1', '0', '0', '0', '0'],
#  ['0', '1', '1', '1', '0', '1', '0'],
#  ['1', '1', '1', '1', '1', '1', '1'],
#  ['0', '1', '1', '1', '0', '1', '0'],
#  ['0', '0', '1', '0', '0', '0', '0']]

# 5줄
for x in range(N):
    # 7개의 수
    for y in range(M//2):
        if matrix[x][y] == '1' and matrix[x][M-1-y] == '0':
            matrix[x][y] = '0'
            matrix[x][M-1-y] = '1'

for i in matrix:        # a에서 안쪽 리스트를 꺼냄
    for j in i:    # 안쪽 리스트에서 요소를 하나씩 꺼냄
        print(j, end='')
    print()