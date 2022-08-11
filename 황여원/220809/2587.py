# 평균과 중앙값 구하기

# 다섯개의 정수가 주어지므로 for문을 다섯번 돌면서 정수를 입력받아 리스트에 담아둔다.
num_list = []

for _ in range(5) :
    num = int(input())
    num_list.append(num) 

# 평균 구하기 
avg = sum(num_list) // 5 
    
# 중앙값 구하기 
# 다섯개의 정수가 주어지므로 중앙값은 오름차순으로 정렬된 리스트의 인덱스[2] 
num_list.sort()
print(avg, num_list[2])
