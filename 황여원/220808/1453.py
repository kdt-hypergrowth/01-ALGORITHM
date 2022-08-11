N = int(input())    # 손님 수 
p = list(map(int,input().split())) # 앉고싶은 자리 

cnt = 0 # 거절 당하는 사람 
seat = [] # 피시방 자리 

for i in range(N) : 
    if p[i] in seat : # 앉고 싶은자리에 이미 누가 있으면
        cnt += 1      # 1을 더해준다 
    else :                 
        seat.append(p[i])  

print(cnt)