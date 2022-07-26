# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("3회차/임선주/20220725/0_숫자의개수.txt")

a = int(input())
b = int(input())
c = int(input())
# print(a, b, c)
result = list(str(a * b * c))
# print(result)
# print(result.count(str(1)))
# print(result.count(str(2)))
# print(result.count(str(3)))
for number in range(0, 10):
    print(result.count(str(number)))
# count 함수는 str만 사용 가능하다.