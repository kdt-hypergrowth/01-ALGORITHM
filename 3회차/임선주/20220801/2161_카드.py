# https://www.acmicpc.net/problem/2161

# 1. 제일 위에 있는 카드 버리기 : popleft()
# 2. 제일 위에 있는 카드 제일 아래에 있는 카드 밑으로 옮기기 : queue.append()
# 3. 반복하기
# 4. 카드가 1개 남았을 때 종료

#  큐 풀이
n = int(input())
queue = list(range(1, n+1))

while len(queue) > 1:
    print(queue.pop(0), end=' ')
    queue.append(queue.pop(0))

print(queue[0])

# 덱 풀이
from collections import deque
n = int(input())
queue = deque(range(1, n + 1))

while len(queue) > 1:
    print(queue.popleft(), end=' ')
    queue.append(queue.popleft())
    
print(queue[0])
