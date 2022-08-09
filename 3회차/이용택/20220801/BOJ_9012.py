'''
괄호 문자열 : (, )로만 구성
-> valid / invalid 판별

'''

t = int(input())

for i in range(t):
    case = list(input())
    stack_ = []

    for char in case:
        if char == '(':
            stack_.append(char)
        else:
            if stack_:
                stack_.pop()
            else:  # '('만 담는 리스트에 ')'가 들어오게되면 충돌이 나는 경우로 NO출력
                print('NO')
                break
    else:
        if not stack_:
            print('YES')
        else:
            print('NO')