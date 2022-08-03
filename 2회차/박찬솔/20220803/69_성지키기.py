import sys
sys.stdin = open('69_성지키기.txt')

n,m = map(int,input().split())
castle=[]                            # 성 값을 초기화

for _ in range(n):                   # 초기화된 castle에 n의 반복수만큼
    castle.append(input())           #  input을 넣음 (4)
row = []                             # 행 (가로) ㅡ
col = []                             # 열 (세로) ㅣ (column)

for i in range(n):                   # n의 범위 내 i에서
    row.append("X" not in castle[i]) # X가 없으면 row에 Ture 값 저장
                                     # X가 있으면 row에 False값 저장
for j in range(m):                   # m의 범위 안에서는 i를 고정시켜놓고 j에 따라서 “X”가 있는 지 판단
    col.append("X" not in [castle[i][j] for i in range(n)])
                                     # X가 없으면 row에 Ture 값 저장
                                     # X가 있으면 row에 False값 저장
print(max(sum(row),sum(col)))        # row와 col의 합을 각각 구하여 경비원이 없는 수 출력, 큰 값이 정답