import sys
sys.stdin = open('87_피시방알바.txt')

n = int(input())                               # 테스트케이스
fish_room = list(map(int, input().split()))    # 피시방을 리스트로 만듬
spot = [0] * 101                               # pc방 자리
refused = 0                                    # 거절당함
for i in fish_room:                            # 피시방 자리를 순회하며
    if spot[i] != 0:                           # 자리가 비어있지 않다면
        refused += 1                           # 거절 당한 사람 1명 추가
    else:                                      # 그렇지 않으면 
        spot[i] += 1                           # 자리에 1명 추가
print(refused)                                 # 거절 당하는 사람의 수 출력