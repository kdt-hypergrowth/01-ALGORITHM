# 성적이 주어졌을 때, 최대 점수, 최소 점수, 점수 차이를 구하는 프로그램

# 2
# 5 30 25 76 23 78
# 6 25 50 70 99 70 90

# 반의 수 K
k = int(input())
for index in range(k) : 
    # 학생수 N, 각 학생의 수학 성적 
    n_score = list(map(int,input().split()))
    # 맨 앞의 학생 수 N 과 수학 성적 분리 
    n = n_score[0]
    score = n_score[1:] 

    # 성적 내림차순 정렬 
    score.sort(reverse = True)

    # 최대점수, 최소점수 
    max_score = max(score)
    min_score = min(score)

    # 가장 큰 인접한 점수 차이
    gaps = []
    for i in range(n-1) :   # n 까지 반복하니까 IndexError: list index out of range 발생 
        # 현재 점수에서 그 바로 뒤의 점수의 차이를 gaps 리스트에 저장 
        gap = score[i] - score[i + 1]
        gaps.append(gap)
    largest_gap = max(gaps)

    print(f'Class {index + 1}')
    print(f'Max {max_score}, Min {min_score}, Largest gap {largest_gap}')