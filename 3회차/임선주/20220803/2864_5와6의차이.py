# https://www.acmicpc.net/problem/2864

import sys
sys.stdin = open('20220803/2864_5와6의차이.txt')

# 최솟값 : 모든 6을 5로 착각했을 때
# min : 6 -> 5
# 최댓값 : 모든 5를 6으로 착각했을 때
# max : 5 -> 6

a, b = input().split()
# 'int' object has no attribute 'replace'
# str 상태에서 replace -> int로 형 변형 -> 더하기
min_ = int(a.replace('6', '5')) + int(b.replace('6', '5'))
max_ = int(a.replace('5', '6')) + int(b.replace('5', '6'))

print(min_, max_)
