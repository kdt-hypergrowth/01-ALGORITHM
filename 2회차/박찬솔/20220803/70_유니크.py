import sys
sys.stdin = open('70_유니크.txt')

n = int(input())                        # 참가자 수
first = []                              # 1번째 판
second = []                             # 2번째 판

third = []                              # 3번째 판
for i in range(n):                      # n(5)의 범위 내에서 i에
    a, b, c = map(int, input().split()) # a, b, c(점수)를 정수형으로 공백으로 구분하여 저장
    first.append(a)                     # 1번째 판에 a값 추가
    second.append(b)                    # 2번째 판에 b값 추가
    third.append(c)                     # 3번째 판에 c값 추가

for j in range(n):                      # n(5)의 범위 내에서 j에
    score = 0                           # 점수를 초기화하고
    if first.count(first[j]) == 1:      # 첫번째 판에 같은 수가 없다면 ( 1개만 존재한다면 )
        score += first[j]               # score 점수 추가
    if second.count(second[j]) == 1:    # 같은 수가 없다면 ( 1개만 존재한다면 )
        score += second[j]              # score 점수 추가
    if third.count(third[j]) == 1:      # 같은 수가 없다면 ( 1개만 존재한다면 )
        score += third[j]               # score 점수 추가

    print(score)                        # 최종 점수 출력