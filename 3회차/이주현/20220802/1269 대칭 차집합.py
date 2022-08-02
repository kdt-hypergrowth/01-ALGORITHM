
A , B = map(int,input().split())

A_list = list(map(int,input().split()))
B_list = list(map(int,input().split()))

A_B = list(set(A_list)-set(B_list))
B_A = list(set(B_list)-set(A_list))

print(len(A_B)+len(B_A))





