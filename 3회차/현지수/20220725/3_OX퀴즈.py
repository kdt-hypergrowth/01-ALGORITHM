# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input()) # 5
for test_case in range(1, T + 1):
    word = input()
    base = 0 # O가 연속될때 쓰일 값
    result = 0 # 총합, 결과
    for i in range(len(word)):
        if word[i] == 'O': # 인덱스가 O일 때
            base += 1 # 1씩 증가
            result += base # 위 값을 결과값에 더함
        elif word[i] == 'X':
            base = 0 # X일 때는 0으로 끊어주기 / 결과값은 그대로
    print(result)