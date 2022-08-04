# 변수 n => list로 설정
n = []
# for 문으로 0~9까지 반복
for i in range(10):
# a에 값을 입력받음    
    a = input()
# b = a에 입력받은 값을 42로 나눠줌. 
    b = a % 42 

# b에서 나온 나머지값을 n에 넣고 싶음.

# 서로 다른 값이 몇 개 있는지 출력..
print()


# ----------------------------------------
# 정답
arr = []
for i in range(10):
    n = int(input())
    arr.append(n % 42)
arr = set(arr)
print(len(arr))