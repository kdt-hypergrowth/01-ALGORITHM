# 1) 문제를 읽고 이해한다
# N의 수를 받아 오름차순으로 바꿔라!

# 2) 문제를 익숙한 용어로 재정의한다
# range(N)
# lst = []
# append

# 3) 어떻게 해결할지 계획을 세운다
# 반복문에서 N에 범위를 받아 
# 그 수만큼 정수들을 받아주고
# 빈 리스트를 만들어 
# append 해준 뒤
# 오름차순으로 바꾼다

# 4) 프로그램으로 구현한다
N = int(input())
M = []
for i in range(N):
    M.append(int(input()))
M = sorted(M)
for j in range(len(M)):
    print(M[j])

# 5) 어떻게 풀었는지 돌아보고, 개선할 방법이 있는지 찾아본다
# 반복문으로 N만큼 정수를 반복하여 받아주고
# 받은 수들을 빈 리스트에 추가시키고 그 리스트들을 soted를 통해
# 오름차순으로 정렬해주고, 정렬한 수의 길이를 반복문에서 입력하고
# 프린트문에서 M[j]를 순회시켜면서 출력