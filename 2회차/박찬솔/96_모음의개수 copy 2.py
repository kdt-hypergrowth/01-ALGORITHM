import sys
sys.stdin = open('96_모음의개수.txt')

vowels = ['a','e','i','o','u'] #모음 리스트 만들기

while True: 
    stc = list(input().lower())  #소문자 형태로 문장 input 받음
    cnt = 0  #모음의 개수

    if stc[0] == '#':   #첫번째 인덱스에 #있으면 종료
        break

    for i in stc: 
        if i in vowels:  #변수 i가 모음리스트에 있으면
            cnt += 1
    
    print(cnt)