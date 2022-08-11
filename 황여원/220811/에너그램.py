# 3
# blather reblath
# maryland landam
# bizarre brazier

n = int(input())
for _ in range(n) : 
    # 두 문자를 입력받고 
    a, b  = input().split()
    # 리스트 형태로 바꿔준다 (한 글자씩 비교해주기 위해)
    list_a = list(a)
    list_b = list(b) 

    # 리스트 형태의 단어들을 정렬해준 후 같은지 아닌지 비교하면 됨 !
    if sorted(list_a) == sorted(list_b) : 
        print(f'{a} & {b} are anagrams.')
    else : 
         print(f'{a} & {b} are NOT anagrams.')


    