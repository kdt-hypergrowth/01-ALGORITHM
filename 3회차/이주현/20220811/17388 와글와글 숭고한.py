#https://www.acmicpc.net/problem/17388



x,y,z = map(int,input().split())

if x + y + z >= 100:
    print('OK')
else:
    if min(x,y,z) == x:
        print('Soongsil')
    elif min(x,y,z) == y:
        print('Korea')
    else:
        print('Hanyang')