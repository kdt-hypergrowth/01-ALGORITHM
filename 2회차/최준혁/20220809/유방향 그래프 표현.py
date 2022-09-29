from pprint import pprint

N, M = map(int, input().split())
matrix = [[0] * N for _ in range(N)]
adj_list = [[] for _ in range(N)]
edges = []

for i in range(M):
    u, v = map(int, input().split())
    edges.append([u, v])
    adj_list[u].append(v)

for edge in edges:
    v1, v2 = edge[0], edge[1]
    matrix[v1][v2] = 1

pprint(matrix)
print(adj_list)