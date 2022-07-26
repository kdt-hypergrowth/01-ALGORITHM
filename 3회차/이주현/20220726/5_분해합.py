# # https://www.acmicpc.net/problem/2231
# import sys

# sys.stdin = open("5_분해합.txt")

# a = sys.stdin.read()
# print(a,type)


n = int(input())

for i in range(n):
    temp = sum(map(int,str(i)))
    
    result = i + temp
   
    if result == n:
        print(i)
        break
else:
    print(0)


