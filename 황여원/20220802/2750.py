import sys
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬
n = int(input())
list_ = []

for _ in range(n) : 
    list_.append(int(sys.stdin.readline()))  

result = sorted(list_)

for i in result : 
    print(i)

