# https://www.acmicpc.net/problem/2577
# import sys

# sys.stdin = open("0_숫자의개수.txt")

a = input()
b = input()
c = input()
a = int(a)
b = int(b)
c = int(c)
result = a * b * c

result_str = str(result)

print(result_str.count('0'))
print(result_str.count('1'))
print(result_str.count('2'))
print(result_str.count('3'))
print(result_str.count('4'))
print(result_str.count('5'))
print(result_str.count('6'))
print(result_str.count('7'))
print(result_str.count('8'))
print(result_str.count('9'))