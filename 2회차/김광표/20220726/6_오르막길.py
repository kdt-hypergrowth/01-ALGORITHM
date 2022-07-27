# 2846 오르막길 B1
import sys

sys.stdin = open("6_오르막길.txt")

N = int(input())
Pi = list(map(int, input().split()))
Pi.append(0) # 인덱스 초과 방지를 위해 Pi에 0을 하나 추가해줌
uphill = []
h = []
for i in range(N) : 
    uphill.append(Pi[i]) #Pi의 행을 더해줌
    
    if Pi[i] >= Pi[i+1] : # 행을 더하다가 내리막길이 나오면 
        h.append(max(uphill)-min(uphill)) # 이전 오르막길의 크기를 저장
        uphill = [] # 오르막길을 초기화

print(max(h)) # 가장 큰 오르막길 출력