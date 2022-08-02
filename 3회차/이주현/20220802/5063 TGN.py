#https://www.acmicpc.net/problem/5063


# T = int(input())
# for i in range(T):
#     r,e,c = map(int,input().split())
#     if r+c < e:
#         print('advertise')
#     elif r + c == e:
#         print('does not matter')
#     else:
#         print('do not advertise')


case = int(input())

for _ in range(case):
    r, e, c = map(int, input().split())
    if r > e - c:
        print('do not advertise')
    elif r == e - c:
        print('does not matter')
    else:
        print('advertise')
    

