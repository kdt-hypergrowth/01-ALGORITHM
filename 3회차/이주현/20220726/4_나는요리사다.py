# https://www.acmicpc.net/problem/2953

cnt = 0
result = 0

for i in range(5):    # 5명의 참가자
    sum_ = 0
    a = map(int,input().split())  # 4번의 점수를 받음
    a = list(a)         #받은 점수를 리스트로 받음
    for j in range(4): 
        sum_ += a[j]    # 받은 4개의 점수를 더함
    if result < sum_:   
        result = sum_   #기존값보다 sum_값이 크면    result 값을 대신함
        cnt = i+1       # 값이 클 때 cnt의 값이 1 올라감, 즉 3번째 줄이 제일 크다면 값이 3번 더해져서 가장 큰 줄의 행이 나온다. 
print(cnt,result)