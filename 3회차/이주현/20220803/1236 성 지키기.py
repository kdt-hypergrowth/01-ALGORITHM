
n,m = map(int,input().split()) # 3,5
matrix = []

for _ in range(n):                  # 3
    matrix.append(input())          # [[XXX..] [.....] [..X.X]]

guard_n = 0
guard_m = 0
for i in range(n):
    if "X" not in matrix[i]:        # 리스트에 X가 들어있지 않으면 guard_n +=1 이를 통해 행에 필요한 가드를 추가할수있다.
        guard_n += 1

for j in range(m):              #matrix[0][0]~[3][0] [1][0]~[1][3] 과 같은 비교를 통해 한 열에서 가드가 없을 경우 guard_m +=1
    if 'X' not in [matrix[i][j] for i in range(n)]:
          guard_m += 1

print(max(guard_n,guard_m)) #최댓값 출력
      




