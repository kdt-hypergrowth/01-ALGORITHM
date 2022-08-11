# 일곱난쟁이의 합은 100 9명중 두명을 뺀 합이 100이 되어야함 
# list_의 합 - 난쟁이1 - 난쟁이2 = 100 

# 일곱난쟁이의 키 입력받아 리스트에 넣어준다
list_ = []
for i in range(9) : 
    list_.append(int(input()))

for i in list_ : 
    for j in list_ : 
       if sum(list_) - i - j == 100 and i != j :  # 아홉난쟁이의 키는 다르기 때문에 i != j 를 넣어준다
        list_.remove(i)
        list_.remove(j) 

# 오름차순 정렬 
list_.sort()

# 출력형태 맞추기
for i in list_ :
    print(i)
