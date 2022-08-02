#https://www.acmicpc.net/problem/10995

N = int(input())

if N == 1:
    print("*")

else:
    for i in range(N):
        if i % 2 == 0:
            print('* '* N)
        else:
            print(' *' * N)


