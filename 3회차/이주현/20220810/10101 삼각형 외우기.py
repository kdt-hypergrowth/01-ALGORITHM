#https://www.acmicpc.net/problem/10101

x = int(input())
y = int(input())
z = int(input())

if x + y + z != 180:
    print('Error')
elif x== y== z == 60:
    print('Equilateral')
elif x + y + z == 180 and (x==y or y == z or z ==x):
    print('Isosceles')
else:
    print('Scalene')





