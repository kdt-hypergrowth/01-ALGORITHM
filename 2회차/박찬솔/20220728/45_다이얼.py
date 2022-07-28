import sys
sys.stdin = open("45_다이얼.txt")

alpabet = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()

time = 0

for i in range(len(word)): # input받은 알파벳 개수만큼 반복
    for j in alpabet:    # alpabet리스트 안에서 반복
        if word[i] in j:  # 같은 알파벳 나오면
            time += alpabet.index(j) + 3 # 3초씩 더해준다

print(time)