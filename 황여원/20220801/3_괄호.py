# T = int(input())

# for i in range(T):
#     stack = []
#     a=input()
#     for j in a:
#         if j == '(':
#             stack.append(j)
#         elif j == ')':
#             if stack:
#                 stack.pop()
#             else: # 스택에 괄호가 없을경우 NO
#                 print("NO")
#                 break
#     else: # break문으로 끊기지 않은경우 수행한다
#         if not stack: # break문으로 안끊기고 스택이 비어있다면 괄호가 다 맞는거다.
#             print("YES")
#         else: # break안 걸렸더라도 스택에 괄호가 들어있다면 NO이다.
#             print("NO")
t = int(input())
for _ in range(t):
   
    vps = list(input())
    sum_ = 0
    
    # 여는 괄호 "("가 나 나오면 +1 닫는 괄호 ")"가 나오면 -1
    for i in vps:
        if i == "(":
            sum_ += 1
        elif i == ")":
            sum_ -= 1

        # -1이 나오면 NO를 출력 -> ex) 닫는 괄호가 여는 괄호의 개수보다 많은 경우로 ))(((    
        if sum_ < 0:
            print("NO")
            break
   
    #  0 이상의 양수라면 NO를 출력 -> ex) 양수가 나오는 경우는 (((())와 같은 경우이다.
    if sum_ > 0:
        print("NO")
    
    elif sum_ == 0:
        print("YES")