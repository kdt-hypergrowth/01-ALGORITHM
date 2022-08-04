#######오답#########

#n,m input값 받음
n,m = map(int,input().split())
# castle 초기화
castle = []
# n만큼 반복
for _ in range(n):
#input 값 추가
    castle.append(input())
# 행/열 초기화
row = [] 
col = []
# n에서 castle의 i번째 행에서 X없으면 row에 추가
for i in range(n):
    if "X" not in castle[i]:
        row.append("X")

# m에서 castle의 행에서 X없으면 추가...
for j in range(m):
    if "X" not in [castle[i][j]]:
            col.append("X")
            break

print(max(sum(row,col)))

###

n,m = map(int,input().split())
castle=[]

for _ in range(n):
    castle.append(input())

row = []
col = []

for i in range(n):
    row.append("X" not in castle[i])

for j in range(m):
    col.append("X" not in [castle[i][j] for i in range(n)])    

print(max(sum(row),sum(col)))