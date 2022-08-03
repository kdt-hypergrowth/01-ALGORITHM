# https://www.acmicpc.net/problem/1269

import sys
sys.stdin = open('20220802/1269_대칭차집합.txt')

N, M = input().split()

A = list(input().split())
B = list(input().split())

# 차집합
a_b = list(set(A) - set(B))
# print(len(a_b))

b_a = list(set(B) - set(A))
# print(len(b_a))

print(len(a_b) + len(b_a))
