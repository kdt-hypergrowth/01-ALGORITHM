#https://www.acmicpc.net/problem/1652
# room_count = [0,0]
# room = []
# leng_h = 0
# leng_v = 0

# n  = int(input())

# for _ in range(n):
#     room.append(list(map(str,input())))     # n만큼의 행렬을 만든다.

# for i in range(n):
#     for j in range(n):
#         if room[i][j] == '.':           # n x n 에서 .이 있는 만큼 길이를 1 증가시켜준다.
#             leng_h += 1
#         else:
#             leng_h = 0
#         if leng_h == 2:                 # 길이가 2가 된다면 방 갯수를 1 증가시켜준다.
#             room_count[1] += 1
        
#         if room[j][i] == '.':               # 같은 방식으로 행에도 적용한다. 
#             leng_v += 1
#         else:
#             leng_v = 0
        
#         if leng_v == 2:
#             room_count[0] += 1

# print(*room_count)          # 정체 방의 갯수





N = int(input())
metrix = []
cnt = 0
cnt_1 = 0
cnt_2 = 0
row_list = []
col_list = []

for i in range(N):
    metrix.append(list(input()))

for j in range(N):
    for i in range(N-1):
        if 'X' not in metrix[j][i:i+2]: 
            cnt += 1
    row_list.append(cnt)
    cnt = 0
# print(row_list)

for j in range(N):
    for i in range(N-1):
        if 'X' not in metrix[i][j] and 'X' not in metrix[i+1][j]:
            cnt += 1
    col_list.append(cnt)
    cnt = 0
# print(col_list)

for i in row_list:
    if i > 0:
        cnt_1 += 1

for i in col_list:
    if i > 0:
        cnt_2 += 1

print(cnt_1, cnt_2)









