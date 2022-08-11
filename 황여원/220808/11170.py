# N부터 M까지의 수들을 종이에 적었을 때 종이에 적힌 0들을 세는 프로그램

T = int(input())
for test_case in range(T) : 
    N,M = map(int,input().split())
    cnt = 0 
    for num in range (N, M+1) : 
        # 0을 찾기 위해서 문자열로 변환 해주기 
        w = str(num) 
        cnt = cnt + w.count('0')
    print(cnt)