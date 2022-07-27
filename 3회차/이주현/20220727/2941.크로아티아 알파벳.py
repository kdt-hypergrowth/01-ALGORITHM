croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input()

for i in croatia:
    word = word.replace(i,'*')      # 크로아티아 알파벳과 같은 문자열을 *로 대체한다

print(len(word))        # 대체된 문자열의 길이를 측정




