from pprint import pprint

# 인접 행렬 만들기
N, M = map(int,input().split())

graph = []
for i in range(N + 1):
    graph.append([0] * (N+1))

for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = 1

pprint(graph)

# 인접 리스트 만들기
N, M = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M) : 
    u, v = map(int,input().split())
    graph[u].append(v)

pprint(graph)