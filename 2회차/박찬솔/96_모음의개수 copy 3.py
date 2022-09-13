import sys
sys.stdin = open('96_모음의개수.txt')

t = list(map(input()))
cnt = 0
c = [
     'a', 'e', 'i', 'o', 'u',
     'A', 'B', 'I', 'O', 'U'
]
while True:
    for i in range(t):
        if t == c:
            cnt += 1
            if t[0] == '#':
                break
        print(cnt)