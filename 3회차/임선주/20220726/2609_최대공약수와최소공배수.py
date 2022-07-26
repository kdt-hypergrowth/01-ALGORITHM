# https://www.acmicpc.net/problem/2609

a, b = map(int, input().split())

# 최대공약수
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

# 최소공배수
def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))


# 함수 사용
import math
a, b = map(int, input().split())
print(math.gcd(a, b))
print(math.lcm(a, b))