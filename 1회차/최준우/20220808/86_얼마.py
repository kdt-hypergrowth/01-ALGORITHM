# https://www.acmicpc.net/problem/9325

T = int(input())

for test_case in range(T):
    s = int(input())
    n = int(input())

    if n == 0:
        print(s)
    else:
        for i in range(n):
            q, p = map(int, input().split())
            s += q * p
        print(s)