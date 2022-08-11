# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

a = int(input())
b = int(input())
c = int(input())

result = list(str(a*b*c)) # 문자열로 변환, list에 담기 
#print(result)

for num in range(10) :    # 0~9 까지
    print(result.count(str(num))) #count 함수 사용 
    #count함수는 str만 사용가능 - num 을 str로 변환 
