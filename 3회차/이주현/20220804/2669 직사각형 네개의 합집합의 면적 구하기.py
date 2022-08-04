#https://www.acmicpc.net/problem/2669

matrix = [[0]*100 for _ in range(100)]               #   100 x 100 칸의 도화지를 만든다.
cnt = 0
for i in range(4):                                  #x1,y1,x2,y2 의 좌표값을 받는다
        x1,y1,x2,y2 = map(int,input().split())
        for i in range(x1,x2):
            for j in range(y1,y2):                  # 받은 좌표값에 해당하는 부분을 1로 바꿔준다
                matrix[i][j] = 1

for i in range(100):
    for j in range(100):                    # 위치가 1 인 곳을 카운팅 한다.
        if matrix[i][j]==1:
            cnt += 1

print(cnt)

