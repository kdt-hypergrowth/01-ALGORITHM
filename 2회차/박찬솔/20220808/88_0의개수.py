import sys
sys.stdin = open('88_0의개수.txt')

t = int(input())                              # 테스트 케이스 개수
for _ in range(t):                            # 테스트 케이스 순회
    count = 0                                 # 출력 할 0의 개수 할당
    n, m = map(int, input().split())          # 입력 받을 수 n ~ m
    for i in range(n, m + 1):                 # n과 m의 수를 확인
        for j in str(i):                      # n과 m을 문자열로 받아옴
            if j == '0':                      # 0이 있다면
                count += 1                    # count에 1씩 추가
    print(count)                              # 0의 개수 출력