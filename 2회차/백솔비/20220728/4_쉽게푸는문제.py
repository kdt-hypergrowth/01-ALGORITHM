import sys
sys.stdin = open("4_쉽게푸는문제.txt")

A, B = map(int, input().split())

arr = []
num = 1
cnt = 0

while len(arr) <= B:
    arr.append(num)
    cnt += 1
    if cnt == num:
        num += 1
        cnt = 0

print(sum(arr[A-1:B]))
