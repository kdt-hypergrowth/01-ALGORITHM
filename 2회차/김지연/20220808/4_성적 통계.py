T = int(input())

for tc in range(1, T+1):
    max_ = 0
    min_ = 99
    class_ = list(map(int, input().split()))
    class_ = class_[1::]

    for i in range(len(class_)):
        if class_[i] > max_:
            max_ = class_[i]
        if class_[i] < min_:
            min_ = class_[i]

    large = sorted(class_, reverse=True) # 가장 큰 인접한 점수 차이

    max_2 = 0
    for j in range(len(large)-1):
        if large[j] - large[j+1] > max_2:
            max_2 = large[j] - large[j+1]

    print('Class {}'.format(tc))
    print('Max {}, Min {}, Largest gap {}'.format(max_, min_, max_2))