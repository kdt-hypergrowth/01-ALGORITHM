#https://www.acmicpc.net/problem/2979
A,B,C = map(int,input().split())
cost = 0


for i in range(3):
    start,end = map(int,input().split())
    time = abs(end-start)
    if i == 0:
        cost_ = time * A
        cost += cost_
    if i == 1:
        cost_ = time * 2*B
        cost += cost_
    if i == 2:
        cost_ = time * 3*C
        cost += cost_

print(cost)   

    

    
    
    
   