# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	68409	37657	32104	55.910%
# 문제
# 우리는 사람의 덩치를 키와 몸무게, 이 두 개의 값으로 표현하여 그 등수를 매겨보려고 한다. 어떤 사람의 몸무게가 x kg이고 키가 y cm라면 이 사람의 덩치는 (x, y)로 표시된다. 두 사람 A 와 B의 덩치가 각각 (x, y), (p, q)라고 할 때 x > p 그리고 y > q 이라면 우리는 A의 덩치가 B의 덩치보다 "더 크다"고 말한다. 
# 예를 들어 어떤 A, B 두 사람의 덩치가 각각 (56, 177), (45, 165) 라고 한다면 A의 덩치가 B보다 큰 셈이 된다. 
# 그런데 서로 다른 덩치끼리 크기를 정할 수 없는 경우도 있다. 
# 예를 들어 두 사람 C와 D의 덩치가 각각 (45, 181), (55, 173)이라면 몸무게는 D가 C보다 더 무겁고, 
# 키는 C가 더 크므로, "덩치"로만 볼 때 C와 D는 누구도 상대방보다 더 크다고 말할 수 없다.

# N명의 집단에서 각 사람의 덩치 등수는 자신보다 더 "큰 덩치"의 사람의 수로 정해진다. 
# 만일 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1이 된다. 
# 이렇게 등수를 결정하면 같은 덩치 등수를 가진 사람은 여러 명도 가능하다. 
# 아래는 5명으로 이루어진 집단에서 각 사람의 덩치와 그 등수가 표시된 표이다.

"""
입력

5
55 185
58 183
88 186
60 175
46 155

출력
2 2 1 2 5
"""
import sys

sys.stdin = open("_덩치.txt")
# 키와 몸무게가 모두 크다
# x > p 그리고 y > q

# if x> p and y>q:
#     print(a의 덩치가 b보다 크다)

# a,b,c,d 서로 한번씩 비교 해주기

# 각 사람보다 덩치가 큰 사람의 수 = [0] * 사람의 수

# if x> p and y>q:
#     print(a의 덩치가 b보다 크다)
#       b보다 덩치가 큰 사람수 +=1

# 사람의 수 입력
n = int(input())
rank = [0] * n
list_ = []
# 사람의 몸무게와 키
for i in range(n):
    weight, height = list(map(int,input().split()))
    # 리스트에 몸무게와 키를 저장
    list_.append((weight,height))
# 모든 사람을 비교하기 위한 이중반복문
for j in range(n):
    # 기준이 되는 사람
    A = list_[j]
    for k in range(n):
        # 비교가 되는 사람
        B = list_[k]


        # a가 b보다 덩치가 큰지 조건문이 필요합니다
        # b가 a보다 덩치가 작다
        if A[0] > B[0] and A[1] > B[1]:

            #b보다 덩치가 큰 사람이 한명 더 있다 +1
            rank[k] += 1
            print(A[0], B[0], A[1],B[1],rank)

for rank in rank:
    print(rank+1, end=" ")