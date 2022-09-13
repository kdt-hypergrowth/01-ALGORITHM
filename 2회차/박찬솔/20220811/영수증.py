import sys
sys.stdin = open('영수증.txt')

x = int(input())    # 총 금액
n = int(input())    # 물건 종류 수
c = []

for i in range(n):
    a, b = map(int,input().split())
    c.append(a * b)

s = sum(c)
if s == x:
    print('Yes')
else:
    print('No')