#https://www.acmicpc.net/problem/25304
final_total = 0
total = int(input())
n = int(input())

for i in range(n):
    cost,ones = map(int,input().split())
    costs = cost * ones
    final_total += costs

if total == final_total:
    print('Yes')
else:
    print('No')
