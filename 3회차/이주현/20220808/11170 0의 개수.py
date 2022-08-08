# https://www.acmicpc.net/problem/11170

T = int(input())            # T만큼 시행

for _ in range(T):
    cnt = 0                     # for 문안에  cnt를 넣어야 한번하고 cnt초기화 가능

    N,M = map(int,input().split())      # N M 숫자 2개 받음
    for i in range(N,M+1):          # 받은 숫자 사이구간을 시행
        word = str(i)               # 받은 숫자를 문자열로 만들어서 0의 유무를 샘
        cnt += word.count('0')

    print(cnt)

