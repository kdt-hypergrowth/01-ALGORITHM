n = int(input())

room = [list(input()) for _ in range(n)]

r, c = 0, 0

for i in range(n) :
    r_cnt, c_cnt = 0, 0 
    
    for j in range(n) : 
        # 가로
        if room[i][j] == '.' :
            r_cnt += 1 
        elif room[i][j] == 'X' :
            r_cnt = 0 
        if r_cnt == 2 :
            r += 1
       
        # 세로
        if room[j][i] == '.' :
            c_cnt += 1 
        elif room[j][i] == 'X' :
            c_cnt = 0 
        if c_cnt == 2 :
            c += 1
            
print(r,c)