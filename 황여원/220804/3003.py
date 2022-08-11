# 체스는 총 16개의 피스를 사용하며, 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
# 예제  입력 - 0 1 2 2 2 7 
#      출력 - 1 0 0 0 0 1
#      입 - 2 1 2 1 2 1
#      출 - -1 0 0 1 0 7

chess = [1, 1, 2, 2, 2, 8]
user_input = list(map(int,input().split()))

for i in range(6):
    print(chess[i] - user_input[i], end =' ')