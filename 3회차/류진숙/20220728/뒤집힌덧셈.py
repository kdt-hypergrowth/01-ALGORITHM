import sys
sys.stdin = open('뒤집힌덧셈.txt')

for i in range(5):

    X, Y = input().split()

    X = int(X[::-1])
    Y = int(Y[::-1])

    result = str(X+Y)[::-1]
    result = int(result)
    print(result)