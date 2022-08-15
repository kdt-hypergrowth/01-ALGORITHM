# https://www.acmicpc.net/problem/1453

import sys
sys.stdin = open('20220808/1453_피시방알바.txt')

N = int(input()) # 손님 수
seats = list(map(int, input().split())) # 원하는 자리

# 중복되는 자리 번호 제거하고 리스트 길이(거절당하지 않은 사람 수) 세기
s = len(set(seats))

# 손님 수에서 거절당하지 않은 사람 수 빼기
print(N - s)
