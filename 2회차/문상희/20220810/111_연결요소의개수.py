vertex, edges = map(int, input().split())
gragh = [[]]
check = [0]
for i in range(vertex):
    gragh += [[]]
    check += [0]
for edge in range(edges):
    i, j = map(int, input().split())
    gragh[i].append(j)
    gragh[j].append(i)

cnt = 1

def dfs(x):
    check[x] = cnt
    for i in gragh[x]:
        if check[i] == 0:
            dfs(i)

for i in range(1, len(check)):
    if check[i] == 0:
        check[i] == cnt
        dfs(i)
        cnt += 1

print(len(set(check)) - 1)