# https://www.acmicpc.net/problem/2750

import sys
sys.stdin = open('20220802/2750_수정렬하기.txt')

N = int(input())
numbers = []

for n in range(N):
    numbers.append(int(input()))
    numbers.sort()
for _ in numbers:
    print(_)


# 오름차순 정렬 min heap

import heapq

# 1) 모든 원소를 차례대로 heap에 삽입한다.
# 2) 힙에 삽입된 모든 원소를 차례대로 result에 담는다.

N = int(input())

