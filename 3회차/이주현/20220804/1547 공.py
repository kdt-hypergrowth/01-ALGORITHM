#https://www.acmicpc.net/problem/1547

ball = [1,2,3]

M = int(input())
for i in range(M):
    a,b = map(int,input().split())

    x1 = ball.index(a)
    y1 = ball.index(b)

    ball[x1],ball[y1] = ball[y1],ball[x1]





print(ball[0])