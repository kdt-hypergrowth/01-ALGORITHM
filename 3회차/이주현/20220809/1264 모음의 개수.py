#https://www.acmicpc.net/problem/1264



list_ = ['a','e','i','o','u']

while True:
    cnt = 0
    my_list = list(input().lower())

    if my_list[0] == "#":
        break
        
    for i in my_list:
        if i in list_:
            cnt += 1

    print(cnt)

