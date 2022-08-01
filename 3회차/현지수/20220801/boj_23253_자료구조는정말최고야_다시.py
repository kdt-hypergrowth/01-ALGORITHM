# 구글링한건데 봐도 모르겠다

N, M = map(int, input().split())
bool = True
for _ in range(M):
    ki = int(input())
    lst = list(map(int, input().split()))
    if bool:
        while len(lst) > 0:
            tmp = lst.pop()
            if lst:
                if tmp > lst[-1]:
                    bool = False
                    break
    else:
        break
if bool:
    print('Yes')
else:
    print('No')