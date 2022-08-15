# https://www.acmicpc.net/problem/5800

import sys
sys.stdin = open('20220808/5800_성적통계.txt')

## 최저 점수가 학생 수로 나와서 성립 안됨
# K = int(input()) # 반의 수

# for k in range(1, K + 1):
#     score = list(map(int, input().split()))

#     for i in range(score[0]):
#         max_score = max(score)
#         min_score = min(score)
#         gap = max_score - min_score

#     print(f'Class {k}')
#     print(f'Max {max_score}, Min {min_score}, Largest gap {gap}')


## 내림차순 정렬해서 최대, 최소 구하기
# K = int(input()) # 반의 수

# for k in range(1, K + 1):
#     score = list(map(int, input().split()))
#     sorted_score = sorted(score, reverse=True) # 최대, 최소, gap 구하기 위해 score 리스트 내림차순 정렬
#     # print(sorted_score)

#     max_score = sorted_score[0]
#     min_score = sorted_score[-2]
#     gap_list = [] # 최대 차이를 구하기 위해 gap 빈 리스트

#     for i in range(len(sorted_score) - 1):
#         gap = sorted_score[i] - sorted_score[i+1]
#         gap_list.append(gap)

#     print(f'Class {k}')
#     print(f'Max {max_score}, Min {min_score}, Largest gap {max(gap_list)}')


# 오름차순 정렬, 리스트 점수만 포함
K = int(input()) # 반의 수

for k in range(1, K + 1):
    score = list(map(int, input().split()))
    score = score[1:] # 학생 수 제외 점수만
    sorted_score = sorted(score) # 최대, 최소, gap 구하기 위해 score 리스트 오름차순 정렬
    # print(sorted_score)

    max_score = sorted_score[-1]
    min_score = sorted_score[0]
    gap_list = [] # 최대 차이를 구하기 위해 gap 빈 리스트

    for i in range(len(sorted_score) - 1):
        gap = sorted_score[i + 1] - sorted_score[i]
        gap_list.append(gap)

    print(f'Class {k}')
    print(f'Max {max_score}, Min {min_score}, Largest gap {max(gap_list)}')