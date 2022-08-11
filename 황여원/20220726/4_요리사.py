cook = 0 
score = 0 

for i in range(5) :  # 다섯명의 요리사 
    a,b,c,d = map(int,input().split()) # 점수 입력
    if score < a+b+c+d : # 현재 점수가 입력된 점수들의 합보다 작으면
        cook = i+1       # 요리사 번호는 i+1 
        score = a+b+c+d  # 점수들의 합이 현재 점수로 바뀐다!
print(cook, score)


# score = []

# for i in range(5) : 
#     score.append(sum(map(int,input().split())))
# print(score.index(max(score))+1, max(score))