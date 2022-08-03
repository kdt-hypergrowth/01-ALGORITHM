#https://www.acmicpc.net/problem/1100

import sys
input = sys.stdin.readline

matrix = []

for _ in range(8):              
    matrix.append(list(map(str,input().split())))       # 8개의 문자열을 받음

result = 0
for i in range(8):                  # 8 X 8 배열
   for j in range(8):
    if (i + j) % 2 == 0:                # i,j 위치/2 ==0 (하얀칸의 위치)
        if matrix[i][j]=='F':               # F가 있으면
            result += 1                         #카운트

print(result)


