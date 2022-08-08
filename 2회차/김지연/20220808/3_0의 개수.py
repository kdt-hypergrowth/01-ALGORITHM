T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    list_ = []
    sep_ = []

    for i in range(N, M+1):
        list_.append(i)

    for j in str(list_):
        sep_.append(j)

    print(sep_.count('0'))