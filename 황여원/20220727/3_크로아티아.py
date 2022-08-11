word = input()
croatia_list = ['c=','c-','dz=','d-','lj','nj','s=','z='] # 크로아티아 알파벳 리스트

for i in croatia_list : 
    # 입력한 문자중에 크로아티아 알파벳이 있으면 
    if i in word  :  
        # replace를 사용해 크로아티아 알파벳과 관련없는 하나의 문자로 변경
        word = word.replace(i, ',') 
# 문자의 길이 출력       
print(len(word))