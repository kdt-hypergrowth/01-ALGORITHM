# 점의 갯수 n 
n = int(input())

# 각 사분면과 축에 있는 점의 개수를 저장할 리스트 변수를 선언
# 인덱스 0에는 축에 있는 점의 개수
# 1~4 에는 각 사분면에 있는 점의 개수 저장 
q_axis = [0, 0, 0, 0, 0]

# 점의 개수 n만큼 반복 
for i in range(n) : 
    xi, yi = map(int,input().split())

    # 1사분면 
    if xi > 0 and yi > 0 :
        q_axis[1] += 1
    # 2사분면 
    elif xi < 0 and yi > 0 :
        q_axis[2] += 1 
    # 3사분면 
    elif xi < 0 and yi < 0 :
        q_axis[3] += 1 
    # 4사분면
    elif xi > 0 and yi < 0 :
        q_axis[4] += 1 
    # 축의 점의 개수 
    elif xi == 0 and yi == 0 :
        q_axis[0] += 1 

print(f'Q1 : {q_axis[1]}')
print(f'Q2 : {q_axis[2]}')
print(f'Q3 : {q_axis[3]}')
print(f'Q4 : {q_axis[4]}')
print(f'AXIS : {q_axis[0]}')