while True : 
    # 소문자로 통일하여 입력받기 
    sentence = list(input().lower())
    cnt = 0
    # 입력의 끝에는 한 줄에 '#' 한 글자가 주어지므로 # 이나오면 break 
    if sentence == '#' :
        break 
    # 문장안에 모음이 있으면 cnt + 1 을 해준다. 
    for i in sentence : 
        if i in 'aeiou' : 
            cnt += 1 
    print(cnt)
 # -> 런타임 에러 

while True : 
    sentence = input()
    cnt = 0
    # 입력의 끝에는 한 줄에 '#' 한 글자가 주어지므로 # 이나오면 break 
    if sentence == '#' :
        break 
    # 문장안에 모음이 있으면 cnt + 1 을 해준다. 
    for i in sentence : 
        if i in 'aeiouAEIOU' : 
            cnt += 1 
    print(cnt)
