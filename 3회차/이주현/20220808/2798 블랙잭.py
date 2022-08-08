#https://www.acmicpc.net/problem/2798

N,M = map(int,input().split())

cards = list(map(int,input().split()))
cards.sort()
total = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if cards[i] + cards[j] + cards[k] > M:
                continue
            else:
                total = max(total,cards[i]+cards[j]+cards[k])

print(total)



