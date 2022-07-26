# https://www.acmicpc.net/problem/2231
import sys

sys.stdin = open("BOJ_2231_input.txt")

N = int(input())
print(N, type(N))
M = list(str(N))
print(M, type(M))
sum_numbers = 0
for number in M:
    int(number)
    print(number)