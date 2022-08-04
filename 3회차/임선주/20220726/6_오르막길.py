# https://www.acmicpc.net/problem/2846

import sys
sys.stdin = open('20220726/6_오르막길.txt')

N = int(input())
hill = list(map(int, input().split()))
top = hill[0]
bottom = hill[0]
height = 0

for n in range(N):
    if hill[n] > hill[n-1]:
        top = hill[n]
    elif hill[n] < hill[n-1]:
        bottom = hill[n]
    height = top - bottom
print(max(height))
        



    
    

