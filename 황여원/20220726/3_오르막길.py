# 인덱싱 [0]부터 시작하면 리스트 맨 끝으로 가기 때문에 [1]부터 시작

# N :리스트 길이
N = int(input())

# 높이 리스트 입력
list_ = list(map(int,input().split()))

# 누적합 저장 변수 
sum_ = 0

# 누적합들을 저장할 리스트 
sum_list = []

# 오르막길을 찾기 위해서 인덱싱
for i in range(1, len(list_)) :
    # 오르막길값은 현재값>이전값 
    if list_[i] > list_[i-1] : 
        # 오르막길의 전체 길이는 부분 오르막길 길이의 누적합
        sum_ = sum_ + list_[i] - list_[i-1] #누적합
        
        # 오르막길 일때마다 누적합 저장 
        #sum_list.append(sum_)

    #오르막길이 아니면
    else : 
        sum_list.append(sum_)
        sum_ = 0 
# 남은 누적합을 저장
sum_list.append(sum_)

# print(sum_list)
# print(max(sum_list))

# 만약 오르막길이 없으면 0 출력
if len(sum_list) == 0 : 
    print(0)
else : 
    print(max(sum_list))