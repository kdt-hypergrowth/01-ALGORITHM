# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")
a,b = map(int,input().split())

# 숫자는 배열이 아니기 때문에 문자열로 변경하고 거꾸로 만든 후 다시 숫자로 변환
c = (int(str(a)[::-1]))
d = (int(str(b)[::-1]))

if c > d :
    print(c)
else :
    print(d)