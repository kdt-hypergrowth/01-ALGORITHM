import sys
sys.stdin = open('86_얼마.txt')

t = int(input())       # 테스트 케이스 개수
for i in range(t):     # 테스트 케이스 내 순회
    s = int(input())   # 첫 줄에 s(자동차 가격) 할당
    n = int(input())   # 둘째 줄 n(서로 다른 옵션) 할당
    price = s          # 첫번째 테스트 케이스 자동차 가격
    for i in range(n): # 둘째 줄 옵션 순회
        q ,p = map(int, input().split())
                       # 특정 옵션과 해당 옵션 할당
        price += q * p # 두번째 테스트 값
        
    print(price)