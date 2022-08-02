# https://www.acmicpc.net/problem/8958

T = int(input())

for i in range(T):
    OX = list(input())
    sum_ = 0
    cnt = 1

    for i in OX:
        if i == 'O':
            sum_ += cnt
            cnt += 1
            
        else:
            cnt = 1 
    print(sum_)



