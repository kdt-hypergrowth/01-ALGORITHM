# https://www.acmicpc.net/problem/11170

import sys
sys.stdin = open('20220808/11170_0의개수.txt')

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    cnt = 0

    for n in range(N, M + 1):
        # 문자 '0'의 개수를 구해야 하기 때문에 str으로 형 변형
        str_n = str(n)
        cnt += str_n.count('0')

    print(cnt)
