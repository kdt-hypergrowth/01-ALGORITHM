# 나머지
# 리스트 활용
# 1. 입력 값 받는 리스트 x 2. 42로 나눈 나머지를 모은 리스트 y 3. 중복값 제거한 리스트 갯수를 모은 리스트 z
x = []
y = []
z = []
for i in range(0, 10):
    x.append(int(input()))
    y.append(x[i] % 42)
    if y[i] not in z:
        z.append(y[i]) 
print(len(z))