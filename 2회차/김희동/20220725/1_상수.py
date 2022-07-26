# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

a, b = map(int, input().split())

print(a, b, type(a), type(b))

number_1 = str(a)[::-1]
print(number_1)
number_2 = str(b)[::-1]
print(number_2)
if number_1 > number_2:
    print(number_1)
if number_1 < number_2:
    print(number_2)