N = int(input())
n = list(map(int, input().split()))
result = []
cnt = 0

for i in range(N):
    if n[i] not in result:
        result.append(n[i])
    else:
        cnt += 1

print(cnt)