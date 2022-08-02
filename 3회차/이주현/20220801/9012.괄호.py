# 성훈
import sys

sys.stdin = open("2_괄호 .txt")

N = int(input())

for i in range(N):
    T = input()
    list_ = []

    for i in T:
        if i == '(':
            list_.append(i)
        elif i == ')':
            if len(list_) != 0:
                list_.pop()
            else:
                print('NO')
                break

    else:
        if len(list_) == 0:
            print('YES')
        else:
            print('NO')

 
            # 주용
t = int(input())
for i in range(t):
    ps = input()
    ps_list = []
    for j in range(len(ps)):
        if ps[j] == '(':
            ps_list.append(ps[j])
        else: # 입력이 )일때
            if ps_list == []: # 리스트가 비어있는 경우 pop할 괄호가 없으므로 그냥 넣음
                ps_list.append(ps[j])
                break
            elif ps_list[-1] == '(': # 마지막 원소가 (일 경우 ()가 완성되므로 (를 pop함
                ps_list.pop()
            else: # 리스트에 )만 남아있는 경우에도 그냥 넣음
                ps_list.append(ps[j])
                
    if len(ps_list) == 0:
        print('YES')
    else:
        print('NO')