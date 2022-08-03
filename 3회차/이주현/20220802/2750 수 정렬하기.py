#https://www.acmicpc.net/problem/2750

T = int(input())            # 입력한 수만큼 반복
a = []
for i in range(T):
    a.append(int(input()))          #  a 라는 리스트에 입력하는 수를 삽입
a = sorted(a)                       # a 리스트를 정렬

for i in range(len(a)):             #정렬한 a리스트를 출력
    print(a[i])







   


