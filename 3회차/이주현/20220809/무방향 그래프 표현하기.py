
N,M = map(int,input().split())

graph = [[0] * N+1 for _ in range(N+1)]

for _ in range(M):
    v1,v2 = map(int,input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1

print(graph)

