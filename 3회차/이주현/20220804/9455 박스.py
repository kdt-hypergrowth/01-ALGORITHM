# https://www.acmicpc.net/problem/9455

chess = [1,1,2,2,2,8]

dong = list(map(int,input().split()))

for i in range(6):
    print(chess[i]-dong[i],end = ' ')




