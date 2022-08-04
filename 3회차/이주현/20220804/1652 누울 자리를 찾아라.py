
room_count = [0,0]
room = []
leng_h = 0
leng_v = 0

n  = int(input())

for _ in range(n):
    room.append(list(map(str,input())))

for i in range(n):
    for j in range(n):
        if room[i][j] == '.':
            leng_h += 1
        else:
            leng_h = 0
        if leng_h >= 2:
            room_count[1] += 1
        
        if room[j][i] == '.':
            leng_v += 1
        else:
            leng_v = 0
        
        if leng_v >= 2:
            room_count[0] += 1

print(*room_count)









