import sys
sys.stdin = open('72_하얀칸.txt')

chess = []
for _ in range(8):                  # 체스판 입력
    chess.append(list(map(str, list(input()))))
                                    # 8x8 크기의 체스판에 입력하는 값들이 들어갈 수 있도록 리스트
answer = 0                          # 초기값 0
for i in range(8):                  # 범위 내에서
    for j in range(8):
        if (i + j) % 2 == 0:        # 체스판 위치가 2로 나누어 떨어지고
            if chess[i][j] == 'F':  # 그 위에 말이 있다면
                answer += 1         # 1씩 증가
print(answer)