# https://www.acmicpc.net/problem/2846
# import sys

# sys.stdin = open("6_오르막길.txt")
# print(sys.stdin.read())

T = int(input())                                # 길의 시점과 종점을 받는다
numbers = list(map(int,input().split()))        # 높낮이를 리스트로 받는다
temp = 0                #누적값을 저장할 변수
a = []

for i in range(1,T):                            
    if numbers[i] > numbers[i-1]:       #길의 좀점이 시점보다 고지대라면 그 차이만큼 temp에 더해준다
        temp += numbers[i] - numbers[i-1]
        if i == T -1:               #마지막 종점에 도착하면 시점,종점 길이차를 리스트에 넣어준다.
            a.append(temp)
    else:
        a.append(temp)              #  종점이 시점보다 값이 작다면 이전까지의 temp를 리스트에 넣어주고 temp를 초기화시킨다.
        temp = 0

print(max(a))                   # 리스트에 추가된 temp 값 중 가장 큰 값을 출력한다.


