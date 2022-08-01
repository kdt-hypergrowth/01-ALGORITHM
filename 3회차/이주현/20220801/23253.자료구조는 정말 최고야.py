#https://www.acmicpc.net/problem/23253



N, M = map(int,input().split())
p = True
for _ in range(M):
    i = int(input())
    k = list(map(int,input().split()))
    for j in range(i-1):
        if k[j] < k[j+1]:
            p = False
            break
    if not p:break


print('Yes' if p else "No")









