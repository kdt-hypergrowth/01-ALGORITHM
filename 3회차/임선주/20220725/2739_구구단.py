# https://www.acmicpc.net/problem/2739

N = int(input())
cnt = 0
for n in range(9):
    cnt += 1
    print(f'{N} * {cnt} = {N * cnt}')
