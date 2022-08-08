#https://www.acmicpc.net/problem/1453

N = int(input())
PC = list(map(int,input().split()))
seats = [0] * 100
refused = 0

for i in PC:
    if seats[i] != 0 :
        refused += 1
    else:
        seats[i] += 1


print(refused)






