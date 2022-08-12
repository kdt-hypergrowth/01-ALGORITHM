#  일과를 마치고 돌아온 난쟁이가 일곱 명이 아닌 아홉 명이었던 것이다.

# 원래는 7명이어야 하지만 9명이 됨

# 다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.

# 난쟁이 7명의 합은 100이다


# 입력
# 아홉 개의 줄에 걸쳐 난쟁이들의 키가 주어진다. 
# 주어지는 키는 100을 넘지 않는 자연수이며, 아홉 난쟁이의 키는 모두 다르며, 
# 가능한 정답이 여러 가지인 경우에는 아무거나 출력한다.

from os import remove


sum_ = []
for i in range(9):
    sum_.append(int(input()))
result = sum(sum_)
sum_.sort()
for i in range(9):
    if len(sum_) ==7:
        break
    for j in range(i +1 , 9 ):
        if 100 ==(result - sum_[i] - sum_[j]):
            remove(sum_[i])    