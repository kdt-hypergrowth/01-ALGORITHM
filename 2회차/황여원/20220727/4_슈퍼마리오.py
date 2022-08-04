# 누적점수 = 0
# for 점수 in 점수리스트 : 
#     누적점수 += 점수
# 차이 = abs(100-누적점수)
#  if 차이 <= 가장 작은 차이 : 
#     가장작은 차이 = 차이
#     가장 큰 누적점수 = 누적점수

scores = []
for i in range(10) :
    score = int(input())
    scores.append(score)

sum_ = 0 
# 가장 작은 차이
min_diff = 10e9

# 가장 큰 누적 점수
max_score = 0

for i in range(10) :
    sum_ += scores[i] # 누적 합

    # 누적 점수와 100의 차이 
    diff = abs(100 - sum_)

    # 차이가 이전의 가장 작은차이보다 작을 때 
    if diff <= min_diff : 
        # 가장 작은 차이와 가장 큰 누적점수를 갱신
        min_diff = diff
        max_score = sum_
# 가장 100 과 가까운 누적 점수 
print(max_score)