# for 문은 너무 많이 나온다 while문 사용 
list_= []
a, b = map(int,input().split())
n = 1 

#수열의 길이가 b 길이보다 작을 때까지 수열에 숫자 추가
while len(list_) < b :
    #n의 크기만큼 수열 리스트에 n을 추기한다 
    for _ in range(n) : 
        list_.append(n) 
    n += 1 
print(list_, len(list_))




# 구간의 시작과 끝
# start, end = map(int,input().split())
# list_ = []
# # 구간의 끝까지 반복
# for i in range(end + 1) : 
#     # i만큼 반복해서 i 가 1 이면 1을 한번 , 2면 2를 두번 list_에 담아준다
#     for j in range(i) : 
#         list_.append(i)
# # print(list_)
# # 시작부터 끝까지의 합 구하기 
# # print(list_[start-1 : end])
# print(sum(list_[start-1 : end]))
