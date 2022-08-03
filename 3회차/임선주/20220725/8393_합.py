# https://www.acmicpc.net/problem/8393

n = int(input())
num = 0
sum = 0

for _ in range(n):
    num += 1
    sum += num
print(sum)
