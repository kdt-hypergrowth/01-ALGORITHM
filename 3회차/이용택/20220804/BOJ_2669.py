# Q. 네개의 합집합의 면적 구하기

import sys
input = sys.stdin.readline

grid = [[0 for _ in range(100)] for _ in range(100)]
result = 0

for _ in range(4):
    x1, y1, x2, y2 = map(lambda x : int(x) - 1, input().split())
    
    for i in range(x1, x2):
        for j in range(y1, y2):
            grid[i][j] = 1

for i in range(100):
    result += grid[i].count(1)
print(result)

# for i in range(100):
#     for j in range(100):
#         if grid[i][j]:
#             result += 1