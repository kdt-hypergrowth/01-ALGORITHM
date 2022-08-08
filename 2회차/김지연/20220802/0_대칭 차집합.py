A, B = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

result = a ^ b
print(len(result))