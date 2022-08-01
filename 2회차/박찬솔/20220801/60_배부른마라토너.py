import sys
sys.stdin = open('60_배부른마라토너.txt')

n = int(input())

person = dict() # 참가한 사람들의 dict
finish = dict() # 완주한 사람들의 dict
answer = ""     # Key: 참가자 이름, Value: 1
for _ in range(n):       # 완주한 사람
    name = input()
    if name in person :
        person[name] += 1 # 동일한 이름의 참가자가 있다면 Value 값을 1 증가
    else :
        person[name] = 1  # 그렇지 않으면 그대로

for _ in range(n-1):     # 참가한 사람
    name = input()
    if name in finish:
        finish[name] += 1
    else :
        finish[name] = 1


for n in person.keys(): # 참가자에는 있지만 완주자에는 없다면 해당 키가 정답
    if n not in finish:
        answer = n
        break
    else:                # 참가자의 value와 완주자의 value가 다르다면 해당 키가 정답
        if person[n] != finish[n]:
            answer = n
            break
print(answer)