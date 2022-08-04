# https://www.acmicpc.net/problem/2851

import sys
sys.stdin = open("3회차/임선주/20220727/11_슈퍼마리오.txt")

# 버섯 점수를 더하기, 100에 가까워지면 stop
# 98, 102 중에서는 더 큰 값(102) 선택
mushroom = []
score = 0

# 10개의 버섯 점수 입력
for i in range(10):
    mushroom.append(int(input()))
    for j in mushroom:
        score += j
        # 합계가 100 이상일 경우
        if score >= 100:
            # 100에 더 가까운 score 구하기
            if (score - 100) > (100 - (score - j)):
                score -= j
print(score)

