# https://www.acmicpc.net/problem/2438

N = int(input())
cnt = 0
asterisk = '*'

for _ in range(N):
    cnt += 1
    star = asterisk * cnt
    print(star)

N = int(input())
for n in range(1, N + 1):
    print('*' * n)
