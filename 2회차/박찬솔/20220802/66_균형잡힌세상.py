import sys
sys.stdin = open('66_균형잡힌세상.txt')

while True:
    str = input()
    if str == '.':                               # 종료 조건을 만나면
        break                                    # break해준다
    stack = []                                   # stack 리스트에 발생 시작되는 괄호 저장
    temp = True                                  # temp = 임시저장공간 변수
    for i in str:                                # 문자열 str에서 괄호 검사
        if i == '(' or i == '[':                 # ( 또는 [
            stack.append(i)                      # stack 리스트에 발생 시작되는 괄호 저장
        elif i == ')':                           # elif를 이용해 ) 검사
            if not stack or stack[-1] == '[':    # 검사를 해주어 대괄호가 오면 스택을 비워나감
                temp = False                     # 스택이 비워져있거나 마지막이 짝이 안맞는다면 temp를 False로 바꿔주고
                break                            # break 해준다
            elif stack[-1] == '(':               # 검사하여 소괄호가 나오면 스택을 비움
                stack.pop()                      # pop를 이용해 요소 삭제
        elif i == ']':                           # 
            if not stack or stack[-1] == '(':    #
                temp = False                     #
                break                            #
            elif stack[-1] == '[':               #
                stack.pop()                      # 
    if temp == True and not stack:               # temp가 True이거나 stack 리스트가 비어있으면 
        print('yes')                             # Yes 출력
    else:                                        # 그렇지 않으면
        print('no')                              # No 출력