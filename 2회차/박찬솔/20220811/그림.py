import sys
sys.stdin = open('그림.txt')

n, m = map(int,input().split())
cnt = 0

for i in range(n+1):