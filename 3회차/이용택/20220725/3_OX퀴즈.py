'''
* 문제 : ox의 정렬에 따른 점수 합산
* 접근
    * 총합에 대한 변수 정의
    * 'O'일 경우 가산점수 누적
    * 'X'일 경우 가산점수 0으로 초기화
* 출처 : https://www.acmicpc.net/problem/8958
'''

import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input())

for i in range(T):
    case = input()
    result = 0
    plus_point = 0

    # 반복문을 순회하며 임의의 요소가 O일 경우 가산점수 누적하여 합산
    # 임의의 요소가 O가 아닌 경우 (X인 경우) 가산점수 0으로 초기화
    for j in case:
        if j == 'O':
            plus_point += 1
            result += plus_point
        else:
            plus_point = 0
    
    print(result)