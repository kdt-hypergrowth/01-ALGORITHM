import sys
import heapq

n = int(input())
q = []

for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    if a != 0:
        heapq.heappush(q, (abs(a), a))
    else:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q)[1])


          
# 주용
import heapq
import sys

heap = []
n = int(sys.stdin.readline())
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap == []:
            print(0)
        else:
            # 최소 힙이므로 가장 작은 값을 pop함
            y = heapq.heappop(heap)
            print(y[0] * y[1])
    else:
        # (x, y)로 push 받았을 시 x가 같은 값이면 y를 정렬함
        # (1, -1), (1, 1) 순으로 정렬
        # x는 입력값의 절댓값, y는 입력값의 부호를 나타냄
        heapq.heappush(heap, (x if x > 0 else -x, 1 if x > 0 else -1))

        # 용택
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

