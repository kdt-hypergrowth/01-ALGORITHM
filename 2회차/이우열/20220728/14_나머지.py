m = {}

for _ in range(10):
    n = int(input())
    m[n % 42] = 1

print(len(m))
