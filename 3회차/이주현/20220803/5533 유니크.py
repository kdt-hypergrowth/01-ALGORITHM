#https://www.acmicpc.net/problem/5533

n = int(input())

score = [[], [], []]

sum = []

for i in range(n):
    a,b,c = map(int,input().split())            
    score[0].append(a)
    score[1].append(b)
    score[2].append(c)          # 점수 개를 받아 각 리스트에 저장
for i in range(n):
    score_ = 0
    for j in range(3):      # 열을 기준으로 (3개의 열) 같은 점수의 개수가 1 이면 더함
        if score[j].count(score[j][i]) == 1:
            score_ += score[j][i]
    sum.append(score_)
# for i in sum:
#     print(i)

print(sum)



