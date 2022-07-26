# https://www.acmicpc.net/problem/1100
# import sys

# sys.stdin = open("7_하얀칸.txt")

T = int(input())
numbers = list(map(int,input().split()))
temp = 0
a = []

for i in range(1,T):
    if numbers[i] > numbers[i-1]:
        temp += numbers[i] - numbers[i-1]
        if i == T -1:
            a.append(temp)
    else:
        a.append(temp)
        temp = 0

print(max(a))




