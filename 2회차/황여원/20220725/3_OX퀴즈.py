# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input()) 
for t in range(T) : 
    ox = input()
    result = 0    # 연속된 o의 갯수
    sum_result = 0 # 점수의 총합
    
    for i in ox : 
        if i == 'O' : 
            result += 1 # 연속된 O 의 갯수 1 증가
            sum_result += result 
        else : 
            result = 0   # x 일때 result 0으로 초기화 
        
    print(sum_result)


