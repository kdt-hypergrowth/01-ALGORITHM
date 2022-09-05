import sys

sys.stdin = open("42_input.txt", "r")
N,M = map(int, input().split())

park_land = [list(input()) for _ in range(N)]
car_break = [0] * 5

di = [0, 1, 1]
dj = [1, 1, 0]

for i in range(N):
    for j in range(M):
        car = 0
        if park_land[i][j] == '#':
            continue

        if park_land[i][j] == 'X':
            car += 1
        

        for d in range(3):
            ni = i + di[d]
            nj = j + dj[d]

            if not(-1< ni < N and -1 < nj < M):
                break

            if park_land[ni][nj] == '#':
                break

            if park_land[ni][nj] == 'X':
                car += 1

        else:
            car_break[car] += 1

print(car_break)


