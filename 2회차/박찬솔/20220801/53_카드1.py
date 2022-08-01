import sys
sys.stdin = open('53_카드1.txt')
from collections import deque

n = int(input())

queue = deque(range(1, n+1))
while len(queue) > 1:
    print(queue.popleft(), end = " ")
    queue.append(queue.popleft())
print(queue[0])