# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

A = int(input()) # 150
B = int(input()) # 266
C = int(input()) # 427

result = list(str(A * B * C))
# [1, 7, 0, 3, 7, 3, 0, 0]

for i in range(10): # 0 ~ 9
    print(result.count(str(i)))
    # i를 문자열로 바꿔서 count함