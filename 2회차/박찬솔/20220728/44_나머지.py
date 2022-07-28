import sys
sys.stdin = open("44_나머지.txt")

n = []                #list설정, 리스트나 튜플은 순서가 있음
for i in range(10):   # 0~9 반복
    a = int(input())  # 변수를 정수로
    b = a % 42        # 입력받은 변수에 42를 더한 나머지 값
    n.append(b)       # n = [39,40,41,0,1,2,40,41,0,1]
s = set(n)            # set로 중복 제거, 정렬
print(len(s))         # 리스트 s의 길이 출력