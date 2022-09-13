import sys

sys.stdin = open("30_나는요리사다.txt")
# 점수를 담을 리스트 score 선언
score = []
# for문을 이용하여 5번 돌면서 참가자의 점수 각각 더해 score에 추가
for i in range(5):
    score.append(sum(map(int, input().split())))
# 우승자의 번호 + 우승자의 점수   
print(score.index(max(score)) + 1, max(score))