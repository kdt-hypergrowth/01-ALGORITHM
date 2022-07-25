# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input()) 
for t in range(1, T + 1) : 
    ox = input()
    result = 0
    sum_result = 0
    for i in ox : 
        if i == 'O' : 
            result += 1 
            sum_result += result 
        else : 
            result = 0   # x 일때 result 0으로 초기화 
        
    print(sum_result)

    # ox = input()
    # result = 0 
    # cnt = 0 
    # for i in range(len(ox)) : 
    #     if ox[i] == 'O' : 
    #         cnt += 1 
    #         result += cnt 
    #     elif ox[i] == 'X' : 
    #         cnt = 0
    # print(result)
