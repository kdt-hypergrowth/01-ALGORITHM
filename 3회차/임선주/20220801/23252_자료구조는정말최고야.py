# https://www.acmicpc.net/problem/23253

import sys
sys.stdin = open("20220801/23252_자료구조는정말최고야.txt")

N, M = list(map(int, input().split()))
# 2 x M줄에 걸쳐 각 더미의 info    
k1 = int(input())
k1_m = list(map(int, input().split()))
k2 = int(input())
k2_m = list(map(int, input().split()))
# 더미가 2개가 아닐 경우 해당 안됨.. 반복문으로 해결해야될 것 같은데 어떻게?
# for _ in range(M):

stack = []


# k1, k2를 별개의 리스트로 설정해서 어떻게 비교해야할 지 모르겠음..
for book in k1_m:
    if book == 1:
        stack.append(book)
    else:
        for book in k2_m:
            if book == 1:
                stack.append(book)

for book in k1_m:
    if 



