a,b = map(int,input().split())
# 파이썬의 내장 함수 map => 여러 개의 데이터를 한 번에 다른 형태로 변환하기 위해서 사용
# map에 int와 input().split()을 넣으면 split의 결과를 모두 int로 변환

# 최대공약수
for i in range(min(a,b),0,-1):
# a,b중 가장 작은 숫자부터 1까지 -1을 하며 for 문 실행
    if a/i == 0 and b/i == 0:
# 만약 a/i, b/i 값이 나머지가 없다면 i=a,b의 최대 공약수
        print(i) 


# 최소공배수
for i in range(max(a,b),(a*b)+ 1):
    # a,b중 더 큰 숫자부터 a*b의 수까지 for 문 실행
    if a/i > 0 and b/i >0:
# a/i, b/i값이 나머지가 있다면 최소공배수
        print(i)
        break
# 여기까지 스스로 해본 풀이 틀림
            

# 정답
# math 모듈을 가져와서 gcd,lcm사용
import math
a,b = map(int,input().split())
print(math.gcd(a,b))
print(math.lcm(a,b))