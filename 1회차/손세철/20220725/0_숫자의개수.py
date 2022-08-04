# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

A = int(input())
B = int(input())
C = int(input())

# A, B, C 각각 입력 받음
multiple= (A*B*C)
result = list(str(multiple))
for i in range (10):
#result 변수 설정 A,B,C 곱한 값을 str으로 변환해서 list로 묶어줌 0부터 각각의 index로 저장

# for문 사용 반복 i =0~9
    print(result.count(str(i)))
# count 사용, str으로 변환 후 str(i) 카운트 해주면 0~9 각각의 개수 출력
