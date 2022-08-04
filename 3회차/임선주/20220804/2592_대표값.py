# https://www.acmicpc.net/problem/2592

import sys
sys.stdin = open('20220804/2592_대표값.txt')

# 평균값
sum = 0

for i in range(10):
    numbers = int(input())
    sum += numbers
print(sum / 10)

# 최빈값
cnt = 0
list_ = []
for j in range(10):
    list_.append(int(input()))
print(list_)

# for j in range(10):
    
# print(max(list_numbers.count(j)))
