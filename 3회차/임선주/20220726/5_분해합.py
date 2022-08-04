# https://www.acmicpc.net/problem/2231

import sys
sys.stdin = open("3회차/임선주/20220726/5_분해합.txt")

N = int(input())
# 생성자 : (100 x a + 10 x b + c) + a + b + c
a = int
b = int
c = int
number = int(100 * a + 10 * b + c)
number_N = int(number + a + b + c)

print(min(number_N))

