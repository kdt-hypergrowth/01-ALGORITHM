# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

a=int(input())
b=int(input())
c=int(input())
n=list(str(a*b*c))
for i in range(10):
    print(n.count(str(i))) 
    #list.count 메서드로 같은 str값의 갯수 출력