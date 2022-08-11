# 영수증 금액 
receipt = int(input())
# 구매한 물건의 종류의 수 
num = int(input())
# 총 금액 
sum_ = 0

for i in range(num) : 
    # 각 물건의 가격 , 갯수 
    a,b = map(int,input().split())
    sum_ += a * b

if sum_ == receipt : 
    print('Yes')
else : 
    print('No')