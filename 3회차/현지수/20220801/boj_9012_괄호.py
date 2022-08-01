import sys
sys.stdin = open("괄호.txt")

T = int(input())
for test_case in range(T):
    n = input()
    stack_ = [] # 스택으로 풀어보자
    bool_ = True
    for i in n:
        if i == '(':
            stack_.append(i) # 여는 괄호일때 스택에 쌓아줌
        else: # 닿는 괄호일때 하나씩 빼주면 되는데
            if len(stack_) == 0: # 빼려면 값이 있어야 하니까 0일 때는 못 뺌
                print('NO') # No 출력하고
                bool_ = False
                break # 반복문 종료
            else: # 뺄 값 있으면
                stack_.pop() # 여는괄호 하나씩 날려주면 됨
    if bool_:
        if len(stack_) == 0: # 그렇게 해서 남은게 없으면
            print('YES') # Yes 출력
        else: # 스택에 남은게 있으면
            print('NO') # No 출력

# len(stack_) == 0 라인이 중복됨
# 불리언 변수를 추가해서 구분하자!
# 대소문자 구분 제발...........