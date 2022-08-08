T = int(input())

for tc in range(1, T+1):
    s = int(input()) # 자동차 가격
    n = int(input()) # 옵션의 개수
   
    for i in range(n):
        q, p = map(int, input().split())
        s += (q*p)
    print(s)