#백준 얼마? 9325
#해빈이는 학교를 다니면서 틈틈히 번 돈으로 자동차를 사려고 한다. 자동차에 여러 가지 옵션을 포함시킬 수 있는데 해빈이는 덧셈과 곱셈을 하지 못하기 때문에 친구 태완이에게 도움을 청했다. 하지만 태완이도 덧셈과 곱셈을 못한다. 불쌍한 이 두 친구를 위해 모든 옵션이 주어진 자동차를 구매하는데 필요한 액수를 계산해 주자.

for TC in range(int(input())):
    Price_ = int(input())
    cost = 0
    for i in range(int(input())):
        q, p = map(int, (input().split()))
        cost += (q*p)
    print(cost+Price_)

