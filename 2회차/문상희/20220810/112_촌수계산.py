people = int(input())
a, b = map(int, input().split())
times = int(input())

gragh = [[]]
check = [0]

for i in range(people):
    gragh += [[]]
    check += [0]
for edge in range(times):
    i, j = map(int, input().split())
    gragh[i].append(j)
    gragh[j].append(i)

cnt = 1
def dfs(x):
    for i in gragh[x]:
        if check[i] == 0:
            check[i] = check[x] + 1
            dfs(i)
dfs(a)
if check[b] == 0:
    print(-1)
else:
    print(check[b])

# for i in range(1, people + 1):
#     if check[i] == 0:
#         check[i] = cnt
#         dfs(i)
#         cnt += 1
# if check[a] != check[b]:
#     print(-1)
# else:

