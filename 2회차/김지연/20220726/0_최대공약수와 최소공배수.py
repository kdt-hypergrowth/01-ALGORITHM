# https://www.acmicpc.net/problem/2609
# import sys  

# sys.stdin = open("0_최대공약수와 최소공배수.txt")
import math 

a, b = input().split() # map 함수 이용해서 int형으로 입력
a = int(a)
b = int(b)
result_A = 0 # 최대공약수를 담을 변수 A
result_B = 0 # 최소공배수를 담을 변수 B

# 첫째 줄 => 두 수의 최대공약수 (각각의 약수 중 공통이며 가장 큰 수)
# 둘째 줄 => 두 수의 최소공배수 (각각의 배수 중 공통이며 가장 작은 수)

for i in range(1, a+1): # 1부터 a만큼 반복
    if (a%i==0) and (b%i==0): # a와 b를 0부터~a까지로 나눴을 때 나머지가 0이면
        result_A = i # result_A를 i로 갱신

print(result_A)

# result_A = math.gcd(a, b) # 최대공약수 구하는 함수

result_B = math.lcm(a,b) # 최소공배수 구하는 함수        
print(result_B)