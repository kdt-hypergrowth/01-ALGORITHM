X, Y = input().split() # 거꾸로 출력하기 위해 string 타입으로 입력

rev_x = X[::-1] # 슬라이싱을 이용해 역순으로 출력
rev_y = Y[::-1] 

result = str(int(rev_x) + int(rev_y))
print(int(result[::-1]))