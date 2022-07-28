# https://www.acmicpc.net/problem/3052

from re import L
import sys
sys.stdin = open('3회차/임선주/20220728/14_나머지.txt')

# 숫자 10개 리스트로 집어넣기
numbers = [int(input()) for n in range(10)]
# print(numbers)
# 42로 나눈 나머지 구하기
remainders = []

for n in numbers:
    remainders.append(n % 42)
    # print(remainders)

# 중복되는 값 제거하기
remainders_set = set(remainders)
# print(remainder_set)
print(len(remainders_set))

# for i in range(10):
#     if remainders[i] != remainders[i-1]:
#         cnt += 1
# print(cnt)


