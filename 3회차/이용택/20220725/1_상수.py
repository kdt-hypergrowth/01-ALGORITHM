'''
* 문제 : 입력을 거꾸로 읽고 숫자 비교하여 큰 수 출력
* 접근
    * 입력 숫자를 뒤집어 대소 비교
    * str(), int() casting 활용
* 출처 : https://www.acmicpc.net/problem/2908
'''

import sys

sys.stdin = open("1_상수.txt")

# 띄어쓰기로 구분하여 두 정수 입력
a, b = input().split()

# 숫자 뒤집고 casting int하여 변수에 저장
reversed_a = int(a[::-1])
reversed_b = int(a[::-1])

# 삼항 연산자를 통해 대소비교
result = reversed_a if reversed_a > reversed_b else reversed_b

print(result)





