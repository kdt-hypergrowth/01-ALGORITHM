# https://www.acmicpc.net/problem/2953
import sys

sys.stdin = open("4_나는요리사다.txt")

score = [] # 점수합이 들어갈 빈 리스트 생성
for i in range(5): # 다섯명의 참가자
    score.append(sum(map(int, input().split()))) # split으로 쪼개고 - map으로 형변환하고 - sum으로 점수 합산한 값을 - score 리스트에 추가
print(score.index(max(score)) + 1, max(score)) # 인덱스 메서드로 최대값의 인덱스 뽑고, 최대값 함수로 최대점수 뽑아서 같이 출력