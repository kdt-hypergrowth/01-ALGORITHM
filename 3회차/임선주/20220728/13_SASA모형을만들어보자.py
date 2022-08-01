# https://www.acmicpc.net/problem/23825

import sys
sys.stdin = open('3회차/임선주/20220728/13_SASA모형을만들어보자.txt')

N = list(map(int, input().split()))
# print(N)

# 2개씩 필요하니까 2로 나눈 몫 구하기
number_s = N[0] // 2
number_a = N[1] // 2

# print(number_s)
# print(number_a)

# number_s //= 2
# number_a //=  2
if number_s > number_a:
    print(number_a)
else:
    print(number_s)

# min()로 할수도 있다!
s, a = map(int, input().split())
print(min(s//2, a//2))

# 한 줄로 끝내기
print(min(map(int, input().split())) // 2)
