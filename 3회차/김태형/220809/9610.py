# 2차원 좌표 상의 여러 점의 좌표 (x,y)가 주어졌을 때, 각 사분면과 축에 점이 몇 개 있는지 구하는 프로그램을 작성하시오.

n = int(input())
Q1 = 0
Q2 = 0 
Q3 = 0
Q4 = 0
AXIS = 0

for i in range(n):
    x, y = map(int,input().split())
    if x>0 and y>0:
        Q1+=1
    if x<0 and y>0:
        Q2+=1
    if x<0 and y<0:
        Q3+=1
    if x>0 and y<0:
        Q4+=1
    if x==0 or y==0:
        AXIS+=1


print(f"Q1: {Q1} \nQ2: {Q2} \nQ3: {Q3} \nQ4: {Q4} \nAXIS: {AXIS}")