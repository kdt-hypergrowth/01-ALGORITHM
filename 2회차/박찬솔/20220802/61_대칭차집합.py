import sys
sys.stdin = open('61_대칭차집합.txt')

# 대칭 차집합의 원소의 개수를 출력
# 두 집합 A와 B가 있을 때, (A-B)와 (B-A)의 합집합을 A와 B의 대칭 차집합
# set 자료형을 정말 유용하게 사용하는 경우는 교집합, 합집합, 차집합을 구할 때
# set는 순서가 없고, 고유한 값, 값이 변하는 객체(mutable)

a, b = map(int, input().split())

a = set(map(int, input().split())) # set를 이용해 교집합을 구한다.
b = set(map(int, input().split())) # set를 이용해 교집합을 구한다.

print(len(a-b) + len(b-a))         # a, b에 대해 a-b와 b-a의 길이를 더 해주면 된다.

# print(len(a^b))                  # 대칭 차집합 구하기