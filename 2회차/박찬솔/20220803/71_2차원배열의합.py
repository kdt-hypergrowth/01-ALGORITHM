import sys
sys.stdin = open('71_2차원배열의합.txt')

# 1 + 2 + 4 + 8 + 16 + 32 = 63 : 1 1 2 3
# 1 + 2                   = 3  : 1 2 1 2
# 1 + 2 + 4 + 8 + 16      = 36 : 1 3 2 3
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
                                             # 리스트 컴프리헨션을 통해 이차원 리스트의 입력을 간단히 받을 수 있음
memo = [[0] * (m+1) for _ in range(n+1)]     # 
 
for i in range(1, n+1):
    for j in range(1, m+1):
        memo[i][j] = matrix[i-1][j-1] + memo[i][j-1] + memo[i-1][j] - memo[i-1][j-1]
 
k = int(input())

for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(memo[x][y] - memo[i-1][y] - memo[x][j-1] + memo[i-1][j-1])