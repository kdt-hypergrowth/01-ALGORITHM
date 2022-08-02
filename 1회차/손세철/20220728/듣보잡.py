import sys 
sys.stdin = open("듣보잡.txt")

# 3 4
# ohhenrie
# charlie
# baesangwook
# obama
# baesangwook
# ohhenrie
# clinton

N,M = list(map(int,input().split()))
print(N,M)
dict_ =dict()
for i in range(N):
    p = input()
    dict_[p] = "듣도못한"

list_ = []
# M의 크기만큼 보도못한 사람 입력
for i in range(M):
    p = input()
    # 입력받은 사람이 딕셔너리의 키 중에 있느냐
    if p in dict_:
        list_.append(p)
list_.sort()
print(len(list_))
for p in list

dict_["ohhenrie"] = "듣도못한사람"
dict_["charlie"] = "듣도못한사람"
dict_["baesangwook"] = "듣도못한사람"

if "obama" in dict_:
    print("obama 듣도보도못한사람")

if "baesangwook" in dict_:
    print("듣도보도못한사람")

if "ohhenrie" in dict_:
    print("듣도보도못한사람")
else:
     "clinton" in dict_