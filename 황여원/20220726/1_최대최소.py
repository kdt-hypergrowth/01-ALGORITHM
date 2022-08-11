a, b = map(int, input().split())

gcd = []
for i in range(1, min(a,b)+1):
    if a % i == 0 and b % i == 0:
        gcd.append(i)
#최대공약수
print(max(gcd))

# 최소공배수 -> 두 수를 곱해서 최대공약수를 나눈 값 
print((a * b) // max(gcd))


# 최대공약수
# -> 유클리드 호제법 : a와 b의 최대공약수 G는 b와 
#                  a%b(a를 b로 나눈 나머지)의 최대공약수 G'과 서로 같다!
# a/b를 후 나머지를 a에 저장
# a와 b의 값을 서로 바꾸고, 다시 a와 b를 나눔 - 나머지 나누기 b를 하기 위함
# 나머지가 0될 때까지 반복 - 나머지가 0이 되면 마지막으로 나누게 된 나머지가 최대공약수

# a, b = map(int, input().split())

# n, m = max(a, b), min(a, b)

# while m > 0:
#     n, m = m, n % m

# print(n)
# print((a * b) // n)
