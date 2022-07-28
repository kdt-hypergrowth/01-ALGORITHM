# https://www.acmicpc.net/problem/1157
# import sys  

# sys.stdin = open("1_단어공부.txt")

str = input()
str_upper = list(str.upper()) # 입력받은 문자열을 모두 대문자로 변경
list_ = []
cnt = 1

for i in range(len(str_upper)):
    if str_upper[i] not in list_: 
        list_.append(str_upper[i])
        cnt = 1
    else:
        cnt += 1
        tmp = cnt
        
if tmp == cnt:
            print('?')
else:
    print(list_)