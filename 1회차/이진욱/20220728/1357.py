
def Rev(n):
    n=str(n)
    n=n[::-1]

    return int(n)

X,Y=map(int,input().split())

print(Rev(Rev(X) + Rev(Y)))
