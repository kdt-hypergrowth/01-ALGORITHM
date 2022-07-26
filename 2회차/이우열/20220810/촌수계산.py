n = int(input())
start, end = list(map(int, input().split()))

m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
stack = []
chonsu = -1
stack.append((start, 0))
visited[start] = True

while stack:
    num, count = stack.pop()
    adj_graph = graph[num]

    if num == end:
        chonsu = count
        break

    for adj in adj_graph:
        if not visited[adj]:
            stack.append((adj, count + 1))
            visited[adj] = True

print(chonsu)

# from collections import deque


# def bfs(start):
#     queue = deque()
#     queue.append(start)
#     while queue:
#         cur = queue.popleft()
#         print(queue)
#         for adj in graph[cur]:
#             if visited[adj] == 0:
#                 visited[adj] = visited[cur] + 1
#                 queue.append(adj)
#                 print(visited)
#                 print(queue)


# n = int(input())
# x, y = map(int, input().split())

# graph = [[] for _ in range(n + 1)]
# visited = [0] * (n + 1)

# m = int(input())
# for _ in range(m):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)

# print(graph)
# bfs(x)

# print(visited[y] if visited[y] != 0 else -1)
