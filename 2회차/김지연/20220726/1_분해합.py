# https://www.acmicpc.net/problem/2231
# import sys  

# sys.stdin = open("1_분해합.txt")

# 분해합 = 생성자 + (생성자의 각 자릿수)

n = int(input()) # 자연수 n 입력
result = 0 

for i in range(1, n+1): # 생성자 1부터 입력값까지 반복
    list_ = list(map(int, str(i))) # i의 각 자릿수를 string으로 형변환해서 리스트에 담음
    result = i + sum(list_) # i값과 i의 각 자릿수를 더해서 result변수에 담음    

    if result==n: # result값과 입력값이 같으면
        print(i) # i값 출력 (생성자)
        break

    if i==n: # i값이 생성자를 찾지 못하고 입력값과 같아지면 0을 출력하고 종료
        print('0')
        break