# 각 알파벳 리스트에 넣음
alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

# for를 사용 반복해서 input 값을 받아 기호 변경  
for i in alphabet:
    word = word.replace(i, "*")

print(len(word))

list_ = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
for char in list_ :
    word = word.replace(char, "*")

print(len(word))