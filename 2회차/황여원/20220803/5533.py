n = int(input())
score = [[], [], []]
sum = []
for i in range(n):
    a, b, c = map(int, input().split())
    score[0].append(a)
    score[1].append(b)
    score[2].append(c)
# print(score)
for i in range(n):
    s_score = 0
    for j in range(3):
        if score[j].count(score[j][i]) == 1:
            s_score += score[j][i]
    sum.append(s_score)
for i in sum:
    print(i)