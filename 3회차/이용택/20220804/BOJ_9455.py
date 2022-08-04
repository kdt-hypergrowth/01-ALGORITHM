'''
Q. 박스
* 아래로 움직임 가능
-> 아래에서 부터 위로 탐색
-> 묶어서 내려가기
'''
import sys
input = sys.stdin.readline

for i in range(int(input())):
    m, n = map(int, input().split())
    case = [list(map(int, input().split())) for _ in range(m)]
    ans = 0  
    
    for j in range(n):
        cnt = 0
        for k in range(m):
            if case[k][j]:
                cnt += 1 
            else:
                ans += cnt  
    print(ans)