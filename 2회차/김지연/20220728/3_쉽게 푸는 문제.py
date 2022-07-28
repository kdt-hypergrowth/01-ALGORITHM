N, M = map(int, input().split())
list_ = []

for i in range(46): # 1부터 1000까지
    for j in range(i):
        list_.append(i) # 숫자 list에 추가

print(sum(list_[N:M+1])) # list_N부터 M까지의 합 출력