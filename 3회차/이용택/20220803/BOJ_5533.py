import sys

input = sys.stdin.readline

# 참가자 수
n = int(input())

card = [list(map(int, input().split())) for _ in range(n)]

score = [0 for _ in range(n)]

for i in range(3):
    target = []
    for j in range(n):
        target.append(card[j][i])
    
    for j in range(n):
        if target.count(card[j][i]) == 1:
            score[j] += card[j][i]
    
for i in score:
    print(i)
