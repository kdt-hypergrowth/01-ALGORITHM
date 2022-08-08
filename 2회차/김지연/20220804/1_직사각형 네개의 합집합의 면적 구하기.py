arr = [[0]*100 for _ in range(100)]

for _ in range(4):
    x1, x2, y1, y2 = map(int, input().split())

    x1, y1, x2, y2 = x1, y1, x2-1, y2-1
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            arr[i][j] += 1

width = 0

for a in range(len(arr)):
    for b in range(len(arr)):
        if arr[a][b] > 0:
            width += 1

print(width)