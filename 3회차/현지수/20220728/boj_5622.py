word = input() # 들어갈 단어 # WA
num = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result = 0 # 걸리는 시간
for i in range(len(word)): # 2
    for j in num: # WXYZ, ABC
        if word[i] in j: # W, A
            result += num.index(j) + 3 # 인덱스는 0~7 # W 할당값 10, A 할당값 3 # (7 + 3) + (0 + 3)
print(result)