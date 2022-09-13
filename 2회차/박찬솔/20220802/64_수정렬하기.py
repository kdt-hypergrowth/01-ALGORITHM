import sys
sys.stdin = open('64_수정렬하기.txt')

n = int(input())
list = []                         # 숫자들을 담기 위한 리스트
for i in range(n):                # 리스트에 n개의 숫자들을
    list.append(int(input()))     # input 추가하여
list.sort()                       # 오름차순 정렬
for i in list:                    # 리스트에 정렬된 n개의 숫자들을
    print(i)                      # 출력하기