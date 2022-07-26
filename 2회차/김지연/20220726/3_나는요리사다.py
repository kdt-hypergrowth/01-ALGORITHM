# https://www.acmicpc.net/problem/2953
# import sys  

# sys.stdin = open("3_나는요리사다.txt")

max_ = 0

for i in range(1, 6):
    list_i = list(map(int, input().split())) # 5명의 평가 점수 입력
    sum_i = sum(list_i) # 5명의 평가 점수 각각 더하기
    if sum_i > max_: # 평가 점수가 max_값보다 크면, 
        max_ = sum_i # max_는 평가점수로 갱신
        cnt = i # 몇 번째 사람인지 출력하기 위해 cnt변수에 몇번째인지 저장
print(cnt, max_)