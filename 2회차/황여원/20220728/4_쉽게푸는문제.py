# 구간의 시작과 끝
start, end = map(int,input().split())
list_ = []
# 구간의 끝까지 반복
for i in range(end + 1) : 
    # i만큼 반복해서 i 가 1 이면 1을 한번 , 2면 2를 두번 list_에 담아준다
    for j in range(i) : 
        list_.append(i)
# print(list_)
# 시작부터 끝까지의 합 구하기 
# print(list_[start-1 : end])
print(sum(list_[start-1 : end]))