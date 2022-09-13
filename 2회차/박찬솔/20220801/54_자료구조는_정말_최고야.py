import sys
sys.stdin = open('54_자료구조는_정말_최고야.txt')

n, m = map(int, input().split())
cnt = True
for _ in range(m):
    i = int(input())
    k = list(map(int, input().split()))
    for j in range(i-1):
        if k[j] < k[j+1]:
            cnt = False
            break
    if not cnt:
        break
print('Yes' if cnt else 'No')