# 쉽게 푸는 문제
import sys
input= sys.stdin.readline

# s는 리스트로 받는게 용이함
# 자릿수가 아닌 숫자의 합을 구해야함
# 문자열로 받게 되면 10이 나올 때 1과 0이 나뉘어져서 더해짐
s = []
a,b = map(int,input().split())
for i in range(0, 1000):
    for _ in range(i):
        s.append(i)
print(sum(list(s)[a-1:b]))