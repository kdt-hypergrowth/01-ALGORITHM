import sys
input = sys.stdin.readline

vowels = ['a','e','i','o','u']

for i in range(3):
    stc = list(input().lower())
    cnt = 0

for j in stc:
    if j in vowels:
        cnt += 1
    if stc[0] == '#':
        break   
print(cnt)