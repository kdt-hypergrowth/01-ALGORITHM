import sys
sys.stdin = open('90_블랙잭.txt')
                                               # Brute-force 장점: 예의x, 100% 정확도
n, m = map(int, input().split())               # 테스트 케이스 윗줄 개수와 합을 할당
num = list(map(int, input().split()))          # 카드의 값
l = len(num)                                   # 카드의 값을 길이로 변환
max_total = 0                                  # 카드의 합
                                               # 완전탐색을 이용
for i in range(0, l-2):                        # 
    for j in range(i + 1, l - 1):              # 
        for k in range(j + 1, l):              # 
            if(num[i] + num[j] + num[k] > m):  # M보다 작거나 같은 경우에는 그 값을 새로운 리스트에 추가
                continue                       # 반복문을 계속 진행
            else:                              # 그렇지 않으면
                max_total = max(max_total, num[i] + num[j] + num[k])
                                               # max()함수를 이용해 가장 큰 값을 출력
print(max_total)                               # 최종 값 출력