# replace를 하기위해 처음에 str으로 입력 받기 
a, b = input().split()

# 합의 최솟값 : 6을 5로 바꿔주면 됨 
sum_min = int(a.replace('6','5')) + int(b.replace('6','5'))
#print(sum_min)

# 합의 최댓값 : 5를 6으로 
sum_max = int(a.replace('5','6')) + int(b.replace('5','6'))

print(sum_min, sum_max)