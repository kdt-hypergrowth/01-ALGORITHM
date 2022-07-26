import sys
input = sys.stdin.readline

matrix = [['O']*100 for _ in range(100)]
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            matrix[i][j] = 'X'

area = 0
for i in range(100):
    area += matrix[i].count('X')
print(area)