# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3회차/임선주/20220725/3_OX퀴즈.txt")

T = int(input())
O = 'O'
X = 'X'
# 'O', 'X' 고정된 입력값을 변수로 저장하면 오타 실수를 방지할 수 있다.

for t in range(T):
    ox = input()
    count_o = 0
    sum_ = 0

    for answer in ox:
        if answer == O:
            count_o += 1 # 연속된 O의 개수 1 증가
            sum_ = count_o + sum_
        if answer == X:
            count_o = 0 # 연속된 O의 개수 초기화(0)

    print(sum_)
