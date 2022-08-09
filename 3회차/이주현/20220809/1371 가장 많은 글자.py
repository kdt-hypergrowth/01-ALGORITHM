#https://www.acmicpc.net/problem/1371

my_list = list(input())

alpha = [0 for _ in range(26)]

# for i in my_list:
#     if i.islower():
#         alpha[ord(i)-97] += 1

# for i in range(26):
#     if alpha[i] == max(alpha):
#         print(chr(i+97),end='')

import sys

s = sys.stdin.read()
li = [0]*26
for c in s:
    if c.islower():
        li[ord(c)-97] += 1
for i in range(26):
    if li[i] == max(li):
        print(chr(97+i), end='')