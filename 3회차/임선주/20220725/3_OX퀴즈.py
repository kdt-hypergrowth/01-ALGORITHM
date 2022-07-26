# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3회차/임선주/20220725/3_OX퀴즈.txt")

T = int(input())
O = 'O'
X = 'X'

for t in range(T):
    ox = input()
    count_o = 0
    sum_ = 0

    for answer in ox:
        if answer == O:
            count_o += 1
            sum_ += count_o
        elif answer == X:
            count_o = 0
            
    print(sum_)
    



