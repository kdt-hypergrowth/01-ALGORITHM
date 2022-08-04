# https://www.acmicpc.net/problem/1100

import sys
sys.stdin = open("20220803/1100_하얀칸.txt")

from pprint import pprint

# matrix 사용
# 방법 1. 일단 초기화
#     8 x 8 [0]
matrix = []
cnt = 0

for _ in range(8):
    line = list(input())
    matrix.append(line)
# matrix = [list(input()) for _ in range(8)]

# 하얀 칸 : (i + j)가 짝수인 칸
for i in range(8):
    for j in range(8):
        if i % 2 == 1 and j % 2 == 1 and line[i][j] == 'F':
            cnt += 1
        elif i % 2 == 0 and j % 2 == 0 and line[i][j] == 'F':
            cnt += 1
print(cnt)


# 방법 2. 입력을 그대로 2D list화
