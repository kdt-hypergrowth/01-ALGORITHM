# https://www.acmicpc.net/problem/25192

import sys
sys.stdin = open('20220802/25192_인사성밝은곰곰이.txt')

N = int(input())
cnt = 0

for n in range(N):
    names = input()
    if names[n - 1] == 'ENTER':
        cnt += 1
        print(cnt)

