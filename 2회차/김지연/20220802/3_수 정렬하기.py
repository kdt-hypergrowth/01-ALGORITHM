N = int(input())
n = []

for i in range(N):
    n.append(int(input()))

n= sorted(n)
print(*n)