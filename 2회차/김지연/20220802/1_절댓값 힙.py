import heapq, sys

N = int(sys.stdin.readline())
heap_ = []

for i in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(heap_) == 0:
            print(0)
        else:
            k = heapq.heappop(heap_)
            print(k[1])
    else: 
        heapq.heappush(heap_,(abs(x), x))

# 이해 X