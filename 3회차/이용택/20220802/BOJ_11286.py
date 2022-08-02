'''
절댓값 힙
1. 배열에 정수 x를 넣음
2. 배열에서 절댓값이 가장 작은 값 출력, 배열에서 제거
- 그 값이 여러개일 때는 원래 값이 가장 작은 수 출력, 제거
'''

import sys
import heapq

input = sys.stdin.readline

n = int(input())

heap = []

for _ in range(n):
    x = int(input())

    if x != 0:
        heapq.heappush(heap, (abs(x), x))  # tuple type으로 push => tuple type[0](==abs(x))를 기준으로 정렬될 것
    
    else:
        if heap:
            print(heapq.heappop(heap)[1])  # tuple type[1] => abs() 하지 않은 원래 x값
        else:
            print(0)
