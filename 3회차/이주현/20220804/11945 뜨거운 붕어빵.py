#https://www.acmicpc.net/problem/11945


N,M = map(int,input().split())
bread = []

for i in range(N):
    bread.append(input())

for i in bread:
    print(i[::-1])

   

