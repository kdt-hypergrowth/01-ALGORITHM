# 2897번 몬스터 트럭

# 지도는 R행 C열의 표로 이뤄져 있다. 
# 표의 각 칸은 빌딩('#'), 주차 된 차('X'), 또는 빈 주차 공간('.')이다. 


# 해빈이를 도와 가능한 주차 공간을 해빈이가 부숴야 하는 차의 수대로 모아서 보여주자. 
# 이때 주차하기 위해 부숴야 하는 차만 고려한다. (주차 하러 가는 길에 부수는 차는 신경쓰지 않는다.) 
# 단, 아무리 몬스터 트럭이라도 빌딩을 부술 수는 없기 때문에 빌딩이 있는 자리에는 주차를 할 수 없다.


# from pprint import pprint

# 입력의 첫 줄에 두 정수 R과 C(2 ≤ R, C ≤ 50)가 주어진다. R은 행의 개수, C는 열의 개수이다.
# 4 4
R, C = map(int, input().split())

# 두 번째 줄에는 R개의 줄에 각각 C개의 문자가 주어진다. 이 문자는 '#', 'X', '.'로만 이뤄져 있다. 
matrix = [list(input()) for _ in range(R)]

# pprint(matrix)
# [['#', '.', '.', '#'],
#  ['.', '.', 'X', '.'],
#  ['.', '.', 'X', '.'],
#  ['#', 'X', 'X', '#']]

# 마지막에 출력해야하는 n0 ~ n4라는 변수를 0으로 정의
n0, n1, n2, n3, n4 = 0, 0, 0, 0, 0

for x in range(R): # 행
    for y in range(C): # 열
        # out of range 방지
        # 리스트 인덱스가 R-1(C-1)까지니까!
        if x+1 == R or y+1 == C:
            break
        
        # 해빈이의 차는 꽤 커서 정확히 2행 2열의 칸을 차지한다.
        a = matrix[x][y]
        b = matrix[x][y+1]
        c = matrix[x+1][y]
        d = matrix[x+1][y+1]

        # 빌딩은 부술수가 없으니까 넘기고 다시 찾기(continue)
        if '#' in [a, b, c, d]:
            continue
        else:
            n = [a, b, c, d].count('X')
            if n == 0:
                n0 += 1
            elif n == 1:
                n1 += 1
            elif n == 2:
                n2 += 1
            elif n == 3:
                n3 += 1
            elif n == 4:
                n4 += 1

# 첫째 줄에는 해빈이가 아무 차도 부수지 않으면서 주차할 수 있는 공간의 개수, n0
print(n0)
# 둘째 줄은 차 한 대를 부수고 주차할 수 있는 공간의 개수, n1
print(n1)
# 셋째 줄은 차 두 대, n2
print(n2)
# 넷째 줄은 차 세 대, n3
print(n3)
# 다섯째 줄은 차 네 대를 부수고 주차할 수 있는 공간의 개수이다. n4
print(n4)

