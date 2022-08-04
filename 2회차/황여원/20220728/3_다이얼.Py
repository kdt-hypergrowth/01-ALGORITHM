# 숫자 1을 누르는데 2초가 걸리고 그 후로 1초씩 증가니까 
# 숫자 2 (A,B,C) 를 누르는건 3초가 걸린다
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

word = input().upper() #WA 입력
sum_ = 0

for i in word: 
    for j in dial: 
        if i in j: 
            sum_ += dial.index(j)+3 #3초를 더해준다 인덱스는 0부터시작

print(sum_) #13!
