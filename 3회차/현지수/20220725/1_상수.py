# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

A, B = input().split() # 스플릿으로 나누기
A = int(A[::-1]) # 형변환없이 바로 리버스
B = int(B[::-1]) # 문자열
if A > B: # 조건문으로 크기 비교 # int
    print(A)
elif B > A:
    print(B)