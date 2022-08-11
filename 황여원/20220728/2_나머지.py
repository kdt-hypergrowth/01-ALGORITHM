na = []

for _ in range(10):
    user_input = int(input())
    # 42 로 나눈 나머지 
    # print(user_input % 42)
    remainder_ = user_input % 42
    # 리스트 안에 담아주고 
    na.append(remainder_)
    # 리스트 중복 제거 
result = set(na)

# 갯수 출력 
print(len(result))