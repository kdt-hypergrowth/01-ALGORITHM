#https://www.acmicpc.net/problem/5063


T = int(input())
for i in range(T):                              # 입력받은 숫자만큼 반복
    r,e,c = map(int,input().split())
    if r+c < e:                         #  광고를 하지 않았을 때 수익(r) + 광고 비용(c)이 광고를 했을 때의 비용(e)보다 크다면
        print('advertise')
    elif r + c == e:
        print('does not matter')
    else:
        print('do not advertise')

