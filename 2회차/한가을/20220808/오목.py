# 2615
# 바둑판에는 19개의 가로줄과 19개의 세로줄이 그려져 있는데
# 가로줄은 위에서부터 아래로 1, 2, ..., 19번의 번호가 붙고
# 세로줄은 왼쪽에서부터 오른쪽으로 1, 2, ..., 19번의 번호가 붙는다
# 같은 색의 바둑알이 연속적으로 다섯 알을 놓이면 그 색이 이긴다
# 연속적이란 가로, 세로 또는 대각선 방향 모두를 뜻함
# 하지만 여섯 알 이상이 연속적으로 놓인 경우에는 이긴 것이 아님
# 입력으로 바둑판의 어떤 상태가 주어졌을 때
# 검은색이 이겼는지 흰색이 이겼는지
# 또는 아직 승부가 결정되지 않았는지 판단하는 프로그램 작성
# 단, 검은색과 흰색이 동시에 이기거나
# 검은색 또는 흰색이 두 군데 이상에서 동시에 이기는 경우는 입력 되지 않음

# 19줄에 각 줄마다 19개의 숫자로 표현
# 검은 바둑알은 1, 흰 바둑알은 2, 알이 놓이지 않는 자리는 0으로 표시

# 첫줄에 검은색이 이겼을 경우에는 1
# 흰색이 이겼을 경우에는 2
# 아직 승부가 결정되지 않았을 경우에는 0 출력
# 검은색 또는 흰색이 이겼을 경우에는
# 둘째 줄에 연속된 다섯 개의 바둑알 중에서
# 가장 왼쪽에 있는 바둑알의 가로줄 번호와
# 세로줄 번호를 순서대로 출력

import sys
sys.stdin  = open('오목.txt')

graph = [list(map(int, input().split())) for _ in range(19)]

#* 오른쪽/아래/대각선 오른쪽 아래/대각선 오른쪽 위
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

def bfs(x, y):
    #* 바둑알의 색
    target = graph[x][y]

    #* 오른쪽/아래/대각선 오른쪽 아래/대각선 오른쪽 위
    #* 4가지 방향 탐색
    for k in range(4):
        #* 바둑알 수
        cnt =1 
        nx = x + dx[k]
        ny = y + dy[k]

        #* 반복문을 통해 오목이 되는지 확인
        while 0 <= nx < 19 and 0 <= ny < 19 and graph[nx][ny] == target:
            cnt += 1

            #* 오목이라면
            if cnt == 5:
                #* 육목 체크
                if 0 <= x - dx[k] < 19 and 0 <= y - dy[k] < 19 and graph[x - dx[k]][y - dy[k]] == target:
                    break
                if 0 <= nx + dx[k] < 19 and 0 < ny + dy[k] < 19 and graph[nx + dx[k]][ny + dy[k]] == target:
                    break

                #* 육목이 아니면 성공한 것으로
                #* 바둑알의 색과 위치를 출력 후 종료
                print(target)
                print(x + 1, y + 1)
                exit(0)

            #* 이전에 이동했던 방향으로 다시 이동
            nx += dx[k]
            ny += dy[k]

#* 반복문을 통해 바둑알이 있는 위치를 탐색
for i in range(19):
    for j in range(19):
        if graph[i][j] != 0:
            bfs(i, j)

print(0)