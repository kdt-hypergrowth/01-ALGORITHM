n = int(input())

# 2차원 리스트 n x 3 행렬
list_ = [[], [], []]
sum = []

for i in range(n):
    a, b, c = map(int, input().split())
 
    list_[0].append(a)
    list_[1].append(b)
    list_[2].append(c)


# 같은수 2개 이상 0점
# 같은수 없으면 점수+


for i in range(n):
    s_score = 0
    for j in range(3):
        if sum[j].count(sum[j][i]) == 1:
            s_score += sum[j][i]
    sum.append(s_score)
for i in sum:


    print(i)
