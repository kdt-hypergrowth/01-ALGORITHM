

FBI = []
for i in range(5):
    a = input()
    if 'FBI' in a:
        FBI.append(a)

if FBI:
    print(*FBI)
else:
    print('HE GOT AWAY!')

    
   


