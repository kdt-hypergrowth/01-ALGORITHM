# 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합
# M의 분해합이 N인 경우, M을 N의 생성자
# 245의 분해합은 256(=245+2+4+5)이 된다.
# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성
import sys

sys.stdin = open("28_분해합.txt")
N = int(input()) # 입력값
result = 0 # 입력값과 비교하기 위한 변수
for i in range(1, N + 1):
    # str함수를 통해 i의 각 자리수를 A 리스트에 넣기
    A = list(map(int, str(i)))
    # 그대로인 값 i와 리스트의 합 더하기
    result = i + sum(A)
    # 합을 더한것과 비교
    if result == N:
        print(i)
        break
    # 생성자가 없다면 0 출력    
    if i == N:
        print(0)

