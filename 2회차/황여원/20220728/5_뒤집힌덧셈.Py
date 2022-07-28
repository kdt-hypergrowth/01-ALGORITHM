# 1. x, y 를 입력받는다
# 2. 뒤집는다 (str)
# 3. 합을 구한다 (int)
# 4. 다시 뒤집는다 (Str)

x, y = input().split()
# 뒤집은 후 두 수를 더해줘야하기 때문에 int로 바꾸기
Rev_x = int(x[::-1])
Rev_y = int(y[::-1])
#print(Rev_x + Rev_y)
# 뒤집기위해서 두 수의 합을 str 으로 바꾸기
# str 인 상태로 입력해보니 5,5 인 경우 01이 출력 됨 -> int로 다시 바꿔준 후 출력  
print(int(str(Rev_x + Rev_y)[::-1]))

