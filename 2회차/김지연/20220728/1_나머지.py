list_ = []

for i in range(10):
    n = int(input())
    n %= 42 # 입력받은 숫자를 42로 나눈 나머지
    
    if n not in list_:
        list_.append(n) # 42로 나눈 나머지가 없으면 list에 추가

print(len(list_)) # list의 총 개수 출력