#사람의 수 n 입력
n = int(input())

list_ = []
# 몸무게, 키 입력
for i in range(n) : 
    w, h = map(int,input().split())
    #리스트에 몸무게, 키 저장
    list_.append((w,h))
# print(list_)

ranks = [0] * n

# 모든 사람을 비교하기 위한 이중 반복문
for a in range(n) : 
    # 기준이 되는 사람 
    A = list_[a] 
    for b in range(n) : 
        # 비교가 되는 사람 
        B = list_[b] 

        # A가 B보다 덩치가 큰지 조건문 
        # B가 A보다 덩치가 작다 
        if A[0] > B[0] and  A[1] > B[1] : 
            # B보다 덩치가 큰 사람이 한명 더 있다 +1 
            ranks[b] += 1
# print(ranks) 
for rank in ranks : 
    print(rank + 1 , end = ' ')