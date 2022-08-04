chess = []
for _ in range(8):
    chess.append(list(map(str, list(input()))))

answer = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0: #하얀칸일 경우 (2로 나누어 떨어질때)
            if chess[i][j] == 'F': #F(말)있을 경우
                answer += 1 # +1씩
print(answer)
