import sys

sys.stdin = open("27_input.txt", "r")
from pprint import pprint
N = int(input())
matrix = [[], [], []]

for _ in range(N):
    a, b, c = map(int, input().split())
    matrix[0].append(a)
    matrix[1].append(b)
    matrix[2].append(c)
print(matrix)
sum_ = []
for i in range(N):
    score = 0
    for j in range(3):
        if matrix[j].count(matrix[j][i]) == 1:
            score += matrix[j][i]
    sum_.append(score)
for i in sum_:
    print(i)
  



        


