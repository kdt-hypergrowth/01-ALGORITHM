import sys
sys.stdin = open('트럭주차.txt')

parking = [0]*101
a, b, c = map(int, input().split())             # 주차 요금 a, b, c

for i in range(3):                              # 3줄
    arrive, leave = map (int, input().split())  # 주차장 들어온 시간, 떠난 시간
    for j in range(arrive-1, leave-1):
        parking[j] += 1
answer = 0
for k in parking:
    if k == 1:
        answer += a * k
    elif k == 2:
        answer += b * k
    elif k == 3:
        answer += c * k    
print(answer)