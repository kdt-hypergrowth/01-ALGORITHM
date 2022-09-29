# 최대공약수와 최소공배수
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

a, b = map(int, input().split())

# 유클리드 알고리즘(Euclidean algorithm)
# : 2개의 자연수의 최대공약수를 구하는 알고리즘, 두 수 중에서 큰 수를 작은 수로 나누는 일을 최종적으로 나머지가 0이 될 때까지 반복하여 최대공약수를 구한다
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(a, b))
print((a*b)//gcd(a, b)) # 최소 공배수 = (두 값 곱한 결과)/최대공약수


