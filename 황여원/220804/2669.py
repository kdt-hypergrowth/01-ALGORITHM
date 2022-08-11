# 0으로 이루어진 빈 도화지 먼저 만들어보기 
paper = [[0]* 100 for _ in range(100)]

# 입력은 4줄이니까 4번 반복
for _ in range(4): 
    x1,x2,y1,y2 = map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            paper[i][j] += 1

sum_ = 0
for row in paper:
    sum_ += sum(row)
print(sum_)