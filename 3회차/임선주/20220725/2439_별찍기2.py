# https://www.acmicpc.net/problem/2439

N = int(input())
star = 0
blank = N

for n in range(N):
    star += 1
    blank -= 1
    print(' ' * blank + '*' * star)


N = int(input())
for n in range(1, N + 1):
    print(' ' * (N - n) + '*' * n)
