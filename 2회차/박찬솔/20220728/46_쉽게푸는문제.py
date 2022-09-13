import sys
sys.stdin = open("46_쉽게푸는문제.txt")

n1, n2 = map(int,input().split())
arr = [0]

for i in range(46): 
    for j in range(i): 
        arr.append(i)
 
print(sum(arr[n1:n2+1]))