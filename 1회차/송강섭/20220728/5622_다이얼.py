number = {         # 전부 다 딕셔너리로 만듬.......
    'A' : 3, 'B' : 3, 'C' : 3,
    'D' : 4, 'E' : 4, 'F' : 4,
    'G' : 5, 'H' : 5, 'I' : 5,
    'J' : 6, 'K' : 6, 'L' : 6,
    'M' : 7, 'N' : 7, 'O' : 7, 
    'P' : 8, 'Q' : 8, 'R' : 8, 'S' : 8,
    'T' : 9, 'U' : 9, 'V' : 9,
    'W' : 10, 'X': 10, 'Y': 10, 'Z': 10
}

word = input()              # 영어 받아옴
result = 0                  # 결과값
for i in word:              # 영어 각 단어 돌려줌
    result += number.get(i) # 단어에 맞는 벨류 가지고와서 결과에 더함
print(result)               # 끝