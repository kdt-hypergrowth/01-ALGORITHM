# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

A = int(input()) # 150
B = int(input()) # 266
C = int(input()) # 427
result = str(A * B * C) # 숫자 자리마다 인덱스 처리해서 순회해야 함 => str이나 list 변환
for i in range(10): # 순회는 for
    cnt = 0 # 기본값 설정
    for a in range(len(result)): # 곱셈한 값의 각 자리 숫자가
        if result[a] == str(i): # 0~9 중 하나와 같다면
            cnt += 1 # 그 자리에 맞춰서 cnt 1씩 증가
    print(cnt)