R, C = map(int, input().split()) # R x C 행렬
car = [input() for _ in range(R)] # 주차장 리스트

res_0 = 0 
res_1 = 0
res_2 = 0
res_3 = 0
res_4 = 0

for i in range(R-1):
    for j in range(C-1):
        car_1 = car[i][j]
        car_2 = car[i][j+1]
        car_3 = car[i+1][j]
        car_4 = car[i+1][j+1]

        sum_ = car_1 + car_2 + car_3 + car_4
        if '#' in sum_:
            pass
        else:
            cnt = sum_.count('X')
            if cnt == 0:
                res_0 += 1
            elif cnt == 1:
                res_1 += 1
            elif cnt == 2:
                res_2 += 1
            elif cnt == 3:
                res_3 += 1 
            elif cnt == 4:
                res_4 += 1

print(res_0)
print(res_1)
print(res_2)
print(res_3)
print(res_4)