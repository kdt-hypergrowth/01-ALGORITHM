import sys
sys.stdin = open('삼각형외우기.txt')

a = int(input())                      # 각 a
b = int(input())                      # 각 b
c = int(input())                      # 각 c

if a == b == c == 60:                 # 세 각의 크기가 모두 60이면
    print(' Equilateral')             # Equilateral

elif a + b + c == 180:                # 세 각의 합이 180이고
    if a == b or b == c or c == a:    # 두 각이 같은 경우에는
        print('Isosceles')            #  Isosceles

    else:
        print('Scalene')              # 같은 각이 없는 경우에는 Scalene

else:
    print('Error')                    # 세 각의 합이 180이 아닌 경우에는 Error