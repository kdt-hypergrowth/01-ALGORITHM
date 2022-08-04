# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

A, B = input().split()
# 입력값을 공백으로 나눔

A = int(A[::-1]) 
B = int(B[::-1])
# 정수로 바꾸고 역순으로

if A > B:
    print(A)
else : 
    print(B)
# A가 더 크면 A출력, 아닐 시 B를 출력

