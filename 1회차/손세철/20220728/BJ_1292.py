A, B = map(int, input().split())
suyeol = []
for i in range(1, 46):
    for _ in range(i):
      suyeol.append(i)

print(sum(suyeol[A-1:B]))