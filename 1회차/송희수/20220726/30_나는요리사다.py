import sys

sys.stdin = open("30_나는요리사다.txt")
target = 0
sum = 0
for i in range(5):
    a, b, c, d = map(int, input().split())

    if sum < a+ b+ c+ d:
        target = i+1
        sum = a + b + c + d

print(target, sum)
