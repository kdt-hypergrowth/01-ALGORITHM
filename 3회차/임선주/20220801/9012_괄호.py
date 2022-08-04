# https://www.acmicpc.net/problem/9012

import sys
sys.stdin = open('20220801/9012_괄호.txt')

T = int(input())

for t in range(T):
    my_list = list(input())

    for _ in my_list:
        if my_list[0] == ')':
            print('NO')
        # else:


 