# https://www.acmicpc.net/problem/1357

import sys
sys.stdin = open('3회차/임선주/20220728/17_뒤집힌덧셈.txt')

# 리스트 N 안에 입력값 넣기
N = input().split()
# print(N)

# 입력값 뒤집고 숫자로 변환
rev_x = int(N[0][::-1])
# print(rev_x)
rev_y = int(N[1][::-1])
# print(rev_y)

# 입력값 더하기
rev_sum = rev_x + rev_y
# print(rev_sum, type(rev_sum))

# 입력값 뒤집고 int로 변환
print(int(str(rev_sum)[::-1]))
