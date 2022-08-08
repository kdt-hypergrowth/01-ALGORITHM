#https://www.acmicpc.net/problem/1436

N = int(input())            

cnt = 0
six_ = 666              # 666에서 시작

while True:                     # 1에서 시작
    if '666' in str(six_):      # 입력받은 정수를 문자열로 변환하였을 떄 666이 있다면
        cnt += 1                # 카운팅 1
    if cnt == N:                # 카운팅이 N에 도달하면
        print(six_)             # six_를 출력한다. (N번째 666이 들어가는 수)
        break
    six_ += 1