
T = int(input())

for i in range(T):
    a,b = map(str,input().split())

    x = sorted(list(a))
    y = sorted(list(b))
    if x == y:
        print(a+' & '+b+' are anagrams.')
    else:
        print(a+' & '+b+' are NOT anagrams.')


