import sys
sys.stdin = open("47_뒤집힌덧셈.txt")

x, y = map(str,input().split())    # 문자열로 입력을 받아 뒤집어준다.
s = str(int(x[::-1]) + int(y[::-1])) # int형으로 변환하여 더해준다음 다시 str형으로 바꿔준다
print(int(s[::-1]))             # 뒤집어준다음 다시 정수형으로 바꿔준다