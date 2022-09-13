import sys
sys.stdin = open('62_절댓값힙.txt')
import heapq                          # 최소 힙(min heap) 자료구조
from sys import stdin


n = int(stdin.readline())
heap=[]                               # heapq 모듈을 이용함으로써 리스트를 최소 힙처럼 다룸
for _ in range(n):
  x = int(stdin.readline())
  if x == 0:
    if heap:
      print(heapq.heappop(heap)[1])   # heappop(), 대상리스트를 넘기면 가장 작은 원소를 삭제하고 값을 리턴
    else:
      print(0)
  else:
    heapq.heappush(heap, (abs(x),x))  # heappush(), 첫번째 인자는 원소를 추가할 대상 리스트, 두번째 인자는 추가할 원소