'''
* 문제 : 임의의 숫자에 쓰인 0~9의 개수 체크
* 접근
    * 임의의 숫자를 str casting하여 for loop 적용
* 출처 : https://www.acmicpc.net/problem/2577
'''

import sys

sys.stdin = open("0_숫자의개수.txt")

# 정수 a, b, c를 라인에 걸쳐 입력받음
a = int(input())
b = int(input())
c = int(input())

# 입력받은 세 변수의 곱, ans 
ans = str(a * b * c)

# ans에 대하여 0 ~ 9 의 각 요소가 몇 개씩 있는지 체크
for i in range(10):
    num = ans.count(str(i))
    print(num) 