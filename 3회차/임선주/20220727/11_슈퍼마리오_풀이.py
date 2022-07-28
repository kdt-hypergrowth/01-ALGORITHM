# https://www.acmicpc.net/problem/2851

import sys
sys.stdin = open("3회차/임선주/20220727/11_슈퍼마리오.txt")

# 버섯 점수를 더하기, 100에 가까워지면 stop
# 98, 102 중에서는 더 큰 값(102) 선택
mushroom = []
score = 0

# 