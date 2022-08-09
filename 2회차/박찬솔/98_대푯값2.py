import sys
sys.stdin = open('98_대푯값2.txt')

x = []                     # 빈 리스트 작성
for i in range(5):         # 0~4
    x.append(int(input())) # 리스트에 하나씩 추가
    x.sort()               # 오름차순
                           # [10, 30, 30, 40, 60]
print(int(sum(x)/5))       # 평균값
print(x[2])                # 0~4 = 중앙: 2