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
    
