# https://www.acmicpc.net/problem/4396

import sys
sys.stdin = open('20220804/4396_지뢰찾기.txt')
# from pprint import pprint # 짧은 리스트는 변화시켜주지 않음

def pprint(list_):

# 8방위 델타리스트
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
y, x = 1, 3

mine = '*'
blank ='.'


for d in range(8):
    dy = 




