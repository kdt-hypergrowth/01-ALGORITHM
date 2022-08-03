
         # A,B 의 숫자열 갯수를 받는다

A_list = list(map(int,input().split()))     # 갯수만큼 입력받은 숫자를 리스트로 만들어 준다
B_list = list(map(int,input().split()))

A_B = list(set(A_list)-set(B_list))     # set을 이용하여 집합의 형태로 만든 후 중복되는 집합들을 빼내어 준다(차집합)
B_A = list(set(B_list)-set(A_list))

print(len(A_B)+len(B_A))        # 길이(갯수)를 더해준다.





