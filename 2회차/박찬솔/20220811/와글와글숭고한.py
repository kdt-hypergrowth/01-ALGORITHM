import sys
sys.stdin = open('와글와글숭고한.txt')

s, k, h = map(int, input().split())

sum = s + k + h

if 100 <= sum:
    print('OK')

elif 100 > sum:
    if s < k <= h or s < h <= k:
        print('Soongsil')

    elif k < s <= h or k < h <= s:
        print('Korea')

    else:
        print('Hanyang')