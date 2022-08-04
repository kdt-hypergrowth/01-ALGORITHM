# https://www.acmicpc.net/problem/2742

N = int(input())
cnt = N + 1

for n in range(N):
    cnt -= 1
    print(cnt)


N = int(input())

for n in range(N):
    print(N - n)

