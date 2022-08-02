import sys
import heapq

n = int(input())
heap = []

for _ in range(n) : 
    #numbers = [1,-1,0,0,0,1,1,-1,-1,2,-2,0,0,0,0,0,0,0]
    numbers = int(sys.stdin.readline())

    if numbers != 0 :
        heapq.heappush(heap, abs(numbers), numbers)
    else : 
        if len(heap) == 0 : 
            print(0)
        else : 
            print(heapq.heappop(heap[1]))