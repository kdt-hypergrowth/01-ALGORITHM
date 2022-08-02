import sys
sys.stdin = open("오르막길.txt")

# N : 리스트 길이
N = int(input())

# 높이 리스트 입력
list_ = list(map(int,input().split()))
# 누적합들을 저장할 리스트
sum_list = []
# 오르막길을 찾기 위해서 인덱싱
for i in range(1,len(list_)):
    # 오르막길은 현재 값 > 이전 값
    if list_[i] > list_[i-1]:
        # 오르막길의 전체 길이는 부분 오르막길 길이의 누적의 합
        sum_ =  sum_ + list_[i] - list_[i-1]
    # 오르막길일때마다 누적합을 저장

    # 오르막길이 아니면
    else:
        sum_list.append(sum_)
        sum_ = 0
print(max(sum_list))

N = int(input())
li = list(map(int, input().split()))
a = 0
re = []
for i in range(N-1):
    if li[i] < li[i+1]:
        a += li[i+1] - li[i]
    else:
        re.append(a)
        a = 0
re.append(a)
print(max(re))