import sys
sys.stdin = open("분해합.txt")


# 숫자 N 입력
N = int(input())

# 1부터 N사이의 모든 수의 분해합을 탐색

for number in range(1,N):
    # print(number)
    # 분해합 저장 변수
    split_sum = 0

    # 각 자리수의 합
    for digit in str(number):
        split_sum = split_sum + int(digit)

    # 분해합은 각 자리수의 합 + 수의 합 => 분해합
    split_sum = split_sum + number

    #구한 분해합과 입력 N이 같으면
    # number는 N의 생성자가됨
    if N == split_sum:
        print(number)
        break # 가장 작은 생성자를 탐색
