import sys
sys.stdin = open('97_사분면.txt')

Q = [0] * 5                            # 출력할 값을 5개로 만듬 (Q0 ~ Q4)
for i in range(int(input())):          # input(5)를 순회하는 for문 작성
    x, y = map(int,input().split())    # 테스트 케이스 내 두번째 줄부터 x,y 할당(5줄)
    if x == 0 or y == 0:               # x, y가 0 일 때
        Q[4] += 1                      # Q4(AXIS)에 점 개수 추가
        continue                       # 계속
    if x > 0:                          # x가 0보다 크고
        if y > 0:                      # y가 0보다 크다면
            Q[0] += 1                  # Q0에 점 개수 추가
        else:                          # 그렇지 않으면
                Q[3] += 1              # Q3에 점 개수 추가
    else:                              # 그렇지 않으면
        if y > 0:                      # y가 0보다 크면
                Q[1] += 1              # Q1에 점 개수 추가
        else:                          # 그렇지 않으면
            Q[2] += 1                  # Q2에 점 개수 추가
                                       # f'string' 을 이용하여 정리 ( format과 비슷함)
print(f"Q1: {Q[0]}\nQ2: {Q[1]}\nQ3: {Q[2]}\nQ4: {Q[3]}\nAXIS: {Q[4]}")