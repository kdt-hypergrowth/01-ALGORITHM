a, b = map(int,input().split()) # 3 7
data = [] # 범위 지정해서 합 구할 리스트

for i in range(b + 1): # 8
    for j in range(i) :
        if len(data) == b :
            break
        data.append(i)
print(sum(data[a - 1 : b]))