# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

a = int(input())
b = int(input())
c = int(input())

number = str(a*b*c)

print(number.count('0'))
print(number.count('1'))
print(number.count('2'))
print(number.count('3'))
print(number.count('4'))
print(number.count('5'))
print(number.count('6'))
print(number.count('7'))
print(number.count('8'))
print(number.count('9'))
