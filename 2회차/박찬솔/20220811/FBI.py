import sys
sys.stdin = open('FBI.txt')

FBI = []

for i in range(1, 6):
    name = input()
    if 'FBI' in name:
        FBI.append(i)
if FBI:
    print(*FBI)            # unpacking

else:
    print('HE GOT AWAY!')