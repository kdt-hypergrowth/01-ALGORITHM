a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

avg = (a + b + c + d + e) / 5

matrix = [a, b, c, d, e]
matrix.sort()

print(round(avg))
print(matrix[2])