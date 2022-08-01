n = int(input())

card = [] 
result = [] # 버린 카드들

for i in range(1, n+1):
    card.append(i)

while len(card) != 1: # 카드 갯수가 1이 될때 까지 반복
    result.append(card.pop(0)) # 가장 위의 카드를 버림
    card.append(card.pop(0)) # 가장 위의 카드를 가장 아래로 옮김

print(*result, card[0])