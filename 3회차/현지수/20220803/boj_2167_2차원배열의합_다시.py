n, m = map(int, input().split())
arr = [list(map(int ,input().split())) for _ in range(n)]
k = int(input())
coor = [list(map(int ,input().split())) for _ in range(k)]

for i in coor:
    sum_val = 0
    for j in range(i - 1, x):
        for k in range(j - 1, y):
            sum_val += arr[j][k]
    print(sum_val)