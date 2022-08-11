# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.  
# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다

# 인접 행렬 만들기
from pprint import pprint

N, M = map(int,input().split())

graph = []
for i in range(N + 1):
    graph.append([0] * (N+1))

for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

pprint(graph)

# 인접 리스트 만들기
N, M = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M) : 
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

pprint(graph)