# https://www.acmicpc.net/problem/7568

N = int(input())
human_list = []

for i in range(N):
    weight,height = map(int,input().split())
    human_list.append((weight,height))

for j in human_list:
    rank = 1
    for k in human_list:
        if j[0] < k[0] and j[1] < k[1]:
            rank += 1
    print(rank,end =' ')


    n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

dict_xy = {k : 0 for k in range(n)}

for i in range(n):
    for j in range(i + 1, n):
        # i가 j보다 덩치가 크면 j보다 덩치가 더 큰 사람 += 1
        if lst[i][0] > lst[j][0] and lst[i][1] > lst[j][1]:
            dict_xy[j] += 1
        # j가 i보다 덩치가 크면 i보다 덩치가 더 큰 사람 += 1
        elif lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            dict_xy[i] += 1
        else:
            pass
        
for i in range(n):
    print(dict_xy[i] + 1, end = ' ')
    
