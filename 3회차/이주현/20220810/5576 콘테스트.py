#https://www.acmicpc.net/problem/5576

w = []
k = []
for i in range(10): 
    a = int(input())
    w.append(a)
for j in range(10):
    b = int(input())
    k.append(b)

w.sort(reverse = True)
k.sort(reverse = True)

wsum = 0
ksum = 0

for i in range(3):
    wsum += w[i]
    ksum += k[i]

print(wsum,ksum)
