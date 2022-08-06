import sys  

sys.stdin = open("3_슈퍼마리오.txt")

sum_ = 0
list_ = []

for i in range(10):
    list_.append(int(input())) # 점수 입력

j = 0
while True: 
    sum_ += list_[j] # 입력한 점수 더하기

    if (sum_==100): # 점수가 딱 100점이면 break
        break
    elif (sum_>100): # 점수가 100점 초과하면
        if sum_-100 <= 100-(sum_-list_[j]): # 현재까지 더한 점수와 전에 더한 점수를 비교해서 
            # 현재까지 더한 점수가 100점과 더 가까우면 break
            break 
        else:
            sum_ = (sum_-list_[j]) # 전에 더한 값이 더 100점과 가까우면 전에 더한 값 출력
            break
    j += 1 
# 둘 중에 더 큰 값 출력 조건
print(sum_)