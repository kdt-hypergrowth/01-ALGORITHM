# 버섯의 점수가 주어졌을 때, 마리오가 받는 점수를 출력하는 프로그램
import sys

sys.stdin = open("34_슈퍼마리오.txt")

m = []
score = 0
for i in range(10):
    m.append(int(input()))
for j in m:
    score += j                 # 차례대로 더해가면서 100이 넘어가는 시점에서 if문을 작성
    if score >= 100:
        if score - 100 > 100 - (score - j):
            score -= j         # 숫자를 비교해 100과 더 가까운 숫자
        break
print(score)