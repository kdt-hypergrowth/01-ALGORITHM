# 1 번째 줄부터 10 번째 줄에는 W 대학의 각 참가자의 점수를 나타내는 정수가
# 11 번째 줄부터 20 번째 줄에는 K 대학의 각 참가자의 점수를 나타내는 정수가 적혀있다. 

w = []
k = []

for i in range(0,10) : 
    w_score = int(input())
    w.append(w_score)
for i in range(0,10) : 
    k_score = int(input())
    k.append(k_score)

w.sort(reverse = True)
k.sort(reverse = True) 

print(w[0]+w[1]+w[2], k[0]+k[1]+k[2])

# 다른사람 풀이
# W = sorted([int(input())for _ in range(10)])[7:]
# K = sorted([int(input())for _ in range(10)])[7:]
# print(sum(W), sum(K))