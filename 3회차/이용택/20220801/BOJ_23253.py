'''
* stack 개념을 못쓰겠음
'''
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

box = []

for i in range(m):
    idx = int(input())  # 인덱스 (더미 번호)
    case = list(map(int, input().split()))  # 라벨링된 책의 리스트
    box.append(case)  # box : 2차원 리스트

for i in range(len(box)):
    if box[i] != sorted(box[i], reverse=True):
        print("No")
        break
else:
    print("Yes")