# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")
T1, T2 = input().split()
T1 = int(T1[::-1]) # 역순
T2 = int(T2[::-1])

# 역순으로 만약 T1이 더 크다면 출력
if T1 > T2: 
    print(T1)
# 그렇지 않으면 T2를 출력    
else:
    print(T2)