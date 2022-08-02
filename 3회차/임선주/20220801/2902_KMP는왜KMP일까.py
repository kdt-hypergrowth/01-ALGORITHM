# https://www.acmicpc.net/problem/2902

import sys
sys.stdin = open('20220801/2902_KMP는왜KMP일까.txt')

name = input()

for _ in name:
    if 64 < ord(_) < 91:
        print(_, end='')