# 9455.
""" 
0 0 0
5 6
1 0 1 1 0 1
0 0 0 0 0 0
1 1 1 0 0 0
0 0 0 1 1 1 
0 1 0 1 0 1
"""
박스 = 1
빈공간 = 0
행개수, 열개수 = 5, 4

박스리스트 = [
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 1, 0, 0],
    [1, 0, 1, 0],
]
이동거리 = 0
# 이중 반복문
# 열부터 순회
for x in range(열개수):
    # 행을 순회, 단, 아래에서 위로 탐색
    # 4 -> 0 -1
    for y in range(행개수-1, -1, -1):
     
        
        # 만약 현재 좌표에 박스가 있으면
        if 박스리스트[y][x] == 박스:
        
#             # 박스 아래에 박스가 없어야 한다.(이동시키는 경우)
            # if 박스리스트[y + 1] != 박스:
                while y + 1 != 행개수 and 박스리스트[y + 1][x] != 박스:
                    박스리스트[y][x] = 빈공간
                    박스리스트[y+1][x] = 박스
                    y += 1
                    이동거리 += 1
print(이동거리)                    
                # 박스가 바닥을 벗어나면 안된다.
                # 리스트의 범위를 벗어나면 안된다.
                # if y + 1 != 행개수:
        
    