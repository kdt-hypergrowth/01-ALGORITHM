import sys
sys.stdin = open("43_SASA 모형을 만들어보자.txt")

A1, A2 = map(int, input().split())
# map으로 나온 결과물에 바로 //2(나눗셈 후 몫을 반환) 연산 후 min에 넣음
print(min(A1//2, A2//2))