# https://www.acmicpc.net/problem/2908
# import sys

# sys.stdin = open("1_상수.txt")

N = int(input())

for tc in range(1, N + 1):
    a, b = map(int, input().split())
    ra = int(str(a)[::-1])
    rb = int(str(b)[::-1])
        
    if ra > rb:
        print(ra)
    else:
        print(rb)