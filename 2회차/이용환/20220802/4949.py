while True:
    Text = input()
    if Text == '.':
        break
    result = []
    for i in Text:
        if i == '(':
            result.append(i)
        elif i == ')':
            if result:
                if result[-1] == '(':
                    result.pop()
                else:
                    print('no')
                    break
            else:
                print('no')
                break        
        elif i == '[':
            result.append(i)
        elif i == ']':
            if result:
                if result[-1] == '[':
                    result.pop()
                else:
                    print('no')
                    break
            else:
                print('no')
                break
        if i == '.':
            if len(result) == 0:
                print('yes')
            else:
                print('no')
