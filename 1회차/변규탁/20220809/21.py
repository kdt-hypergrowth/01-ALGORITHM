

N, M = map(int, input().split())

graph1 =[[0] * (N+1) for _ in range(N+1)]
graph2 = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph1[v1][v2] = 1
    graph1[v2][v1] = 1
    graph2[v1].append(v2)
    graph2[v2].append(v1)


print(graph1)
print(graph2)