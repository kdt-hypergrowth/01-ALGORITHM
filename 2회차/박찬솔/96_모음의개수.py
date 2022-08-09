import sys
sys.stdin = open('96_모음의개수.txt')


c = [
     'a', 'e', 'i', 'o', 'u',
     'A', 'B', 'I', 'O', 'U'
]
while True:

    t1 = input()
    t2 = input()
    t3 = input()
    cnt = 0

    for i in range(t1):
        if t1 == c:
            cnt += 1
        print(cnt)

    for i in range(t2):
        if t2 == c:
            cnt += 1
        print(cnt)

    for i in range(t3):
        if t3 == c:
            cnt += 1
        print(cnt)

    # while True:
    #   eng = input()             # 영어 문장 입력
    # if eng == '#':              # #을 입력 받으면
    #   break                     # 반복문 탈출

    # cnt = 0                     # 모음 개수
    # for c in eng:               # 영어 문장에서
    #   if c in 'aeiouAEIOU':     # 각 문자가 모음에 해당하면
    #       cnt += 1              # 모음 개수 1 증가
    # print(cnt)                  # 최종 모음 개수 출력