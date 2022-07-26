# https://www.acmicpc.net/problem/2846
# import sys  

# sys.stdin = open("2_오르막길.txt")

T = int(input()) # 테스트케이스 int형으로 입력
list_ = list(map(int, input().split())) # list형으로 자전거 길 입력
cnt = 0 # cnt변수에 오르막길의 크기를 담음
tmp = 0 # tmp변수에 오르막길이 끝나는 지점을 담음

for i in range(len(list_)-1): 
    if list_[i] < list_[i+1]: # 오르막길이면 cnt변수에 오르막길의 크기 담음
        cnt += list_[i+1] - list_[i]

    elif list_[i] >= list_[i+1]: # 오르막길이 아니고
        if cnt > tmp: # 전에 저장한 오르막길의 크기보다 현재의 오르막길이 더 크다면
            tmp = cnt # tmp변수에 오르막길의 크기를 새로 갱신
            cnt = 0 # cnt는 초기화
        else: # 전에 저장한 오르막길의 크기가 더 크다면
            cnt = 0 # cnt만 초기화
if tmp > cnt: # 마지막으로 가장 최근의 오르막길 크기를 비교해서 더 큰 값을 가지는 변수 출력
    print(tmp)
else:
    print(cnt)