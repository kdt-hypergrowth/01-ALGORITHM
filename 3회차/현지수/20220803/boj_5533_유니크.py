n = int(input())
num = [[], [], []]
for _ in range(n):
    a, b, c = map(int, input().split())
    num[0].append(a)
    num[1].append(b)
    num[2].append(c) # 행, 열이 아니라 열, 행으로 매트릭스를 만들어야 함

score = [0] * n # 정답 매트릭스 설정 # 리스트는 out of range 오류나서 못 품
for i in range(3): # 행 고정
    for j in range(n): # 열 이동
        if num[i].count(num[i][j]) == 1: # 같은 점수가 존재하지 않으면
            score[j] += num[i][j] # 점수 더해줌
for s in score: # 점수합 순서대로 출력
    print(s)