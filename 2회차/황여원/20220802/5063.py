n = int(input())

# r은 광고를 하지 않았을 때 수익, e는 광고를 했을 때의 수익, c는 광고 비용
# 광고를 해야 하면 "advertise", 하지 않아야 하면 "do not advertise", 
# 광고를 해도 수익이 차이가 없다면 "does not matter"를 출력

for _ in range(n) :
    r, e, c = map(int,input().split())

    # 광고를 했을때의 수익에서 광고 비용을 뺀 값이 광고를 하지 않았을때의 수익이 더 작으면 광고를 해야한다 
    if r < e - c :
        print('advertise')
    # 광고를 했을때의 수익에서 광고 비용을 뺀 값이 광고를 하지 않았을때의 수익이 더 많으면 광고를 하지 않아야 한다
    elif r > e - c :
        print('do not advertise')
    # 그 외 수익의 차이가 없으면 (r = e-c) 
    else : 
        print('does not matter')