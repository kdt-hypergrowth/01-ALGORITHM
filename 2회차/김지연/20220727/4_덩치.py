import sys  

sys.stdin = open("4_덩치.txt")

T = int(input())
list_ = []

for i in range(T):
    x, y = map(int, input().split()) # 키, 몸무게 입력
    list_.append((x, y)) # 키, 몸무게 리스트에 추가

for i in list_: # 이중 반복문으로 한명 한명 비교
    score = 1
    for j in list_:
        if i[0] < j[0] and i[1] < j[1]: 
            # 한 명씩 비교해가면서 키와 몸무게가 둘 다 작으면 score+1
            score += 1
    print(score, end=' ')