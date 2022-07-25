# https://www.acmicpc.net/problem/8958

# O = 1점, X = 0점
# 연속 점수 +1씩 늘어남, 틀릴 시 0점으로 초기화
import sys
sys.stdin = open("3_OX퀴즈.txt")
num = int(input())
# 테스트 개수를 num에 입력받고 그 범위만큼 for문을 반복해준다. 
# problem에 OX문자열을 입력받고
for i in range(5):
   problem = list(input())
   score = 0
   sum = 0
# score와 sum을 0으로 정의해준다.
   for i in problem:
      if i == 'O':
         score += 1
         sum += score
      else:
         score = 0
   print(sum)


   