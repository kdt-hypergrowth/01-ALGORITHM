k = int(input())
for t in range(1,k+1):
    n = list(map(int,input().split()))
    a = n.pop(0)

    l_gap = 0
    for i in range(a-1):
        gap = sorted(n,reverse=True)[i] - sorted(n,reverse=True)[i+1]
        if l_gap < gap:
            l_gap = gap
            
    print(f'Class {t}')
    print(f'Max {max(n)}, Min {min(n)}, Largest gap {l_gap}')
