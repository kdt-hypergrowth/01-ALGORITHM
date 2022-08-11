#https://www.acmicpc.net/problem/2495

numbers = []

for i in range(3):
    num = list(input())
    numbers.append(num)

for i in range(3):
    cnt =1
    mymax = 1
    for j in range(7):
        if numbers[i][j] == numbers[i][j+1]:
            cnt += 1
        else:
            mymax = max(cnt,mymax)
            cnt = 1
       
    print(max(mymax,cnt))

