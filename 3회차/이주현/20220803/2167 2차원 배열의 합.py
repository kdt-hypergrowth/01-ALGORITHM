n,m = map(int,input().split())
matrix = []
count = 0
for i in range(n):
    matrix.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        sum_ = matrix[i][j]
        sum_ = int(sum_)
        count += sum_
        
print(count)