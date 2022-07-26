# 하얀 칸
# 문제 : 체스판의 상태가 주어졌을 때, 하얀 칸 위에 말이 몇 개 있는지 구하기
#      첫째 줄부터 8개의 줄에 체스판의 상태가 주어진다. ‘.’은 빈 칸이고, ‘F’는 위에 말이 있는 칸이다.
#      검정 칸과 하얀 칸이 번갈아가면서 색칠되어 있다. 가장 왼쪽 위칸 (0,0)은 하얀색이다.

chess = [list(input()) for _ in range(8)]

cnt = 0
for x in range(8):
    for y in range(8):
        # 좌표 값을 더하면 짝수, 해당 좌표값이 'F' 라면 1씩 카운팅
        if (x + y) % 2 == 0 and chess[x][y] == 'F':
            cnt += 1

print(cnt)
