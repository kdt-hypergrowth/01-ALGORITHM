import sys
sys.stdin = open('콘테스트.txt')

w = []                  # 대학
k = []                  # 대학
for i in range(0, 10):  # 20 줄 중에서 10줄까지
    a = int(input())    # 인풋 23 23 20 15 15 14 13 9 7 6
    w.append(a)         # W 대학에 인풋 할당

for i in range(0, 10):  # 20 줄 중에서 20줄까지
    b = int(input())    # 인풋 25 19 17 17 16 13 12 11 9 5
    k.append(b)         # W 대학에 인풋 할당

w.sort(reverse=True)    # w대학 오름차순을 반대로 
k.sort(reverse=True)    # k대학 오름차순을 반대로
wsum = 0                # w대학 득점
ksum = 0                # k대학 득점
for i in range(0, 3):   # 0 1 2
    wsum += w[i]        # wsum = 앞에 있는 고득점 3명의 합
    ksum += k[i]        # bsum = 앞에 있는 고득점 3명의 합
print(wsum, ksum)       # w대학과 k대학의 점수