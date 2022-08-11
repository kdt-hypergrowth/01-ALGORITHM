# 5개 줄에 요원의 첩보원명이 주어진다.
p_list = []
for _ in range(5) :
    p_list.append(input()) 

cnt = 0 
for i in range(len(p_list)) : 
    if 'FBI' in p_list[i] : 
        # 해당요원이 몇번째인지 출력 
        print(i + 1, end =' ' )
        cnt += 1 

if cnt == 0 :
    print('HE GOT AWAY!')  

