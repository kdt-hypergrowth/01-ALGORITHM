import sys
sys.stdin = open("0_공약수와최소공배수.txt")

x, y = map(int, input().split())


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return x * y // gcd(x, y)


print(gcd(x, y))
print(lcm(x, y))
