# https://www.acmicpc.net/problem/2798

import sys
sys.stdin = open('20220808/2798_블랙잭.txt')

N, M = map(int, input().split())
cards = list(map(int, input().split()))

def blackjack(N, M, cards):
    sum_ = 0
    max_sum = 0

    for i in range(N - 2): # 첫 번째 카드
        for j in range(i + 1, N - 1): # 두 번째 카드
            for k in range(j + 1, N): # 세 번째 카드
                sum_ = cards[i] + cards[j] + cards[k]

                if max_sum < sum_ <= M:
                    max_sum = sum_

                if sum_ == M:
                    return sum_

    return max_sum

print(blackjack(N, M, cards))
