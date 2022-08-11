n, m = map(int, input().split())

castle = []

for _ in range(n) : 
    line = list(input())
    castle.append(line)
# print(castle)
# XX...
# .XX..
# ...XX

#모든 행, 열에 경비원이 한명 이상 있어야함 
#행기준, 열기준으로 필요한 경비원의 수 구함
row = 0
col = 0

# 행을 반복해서 돌면서 x가 없으면 + 1
for i in range(n) :
    if 'X' not in castle[i] : 
        row += 1 
# print(row)

# 열을 반복해서 돌면서 x가 없으면 +1
for j in range(m) :
    if 'X' not in [castle[i][j] for i in range(n)] :
        col += 1 

# 둘중에 큰 값을 프린트
print(max(row,col))