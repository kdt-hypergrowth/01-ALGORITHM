from collections import deque 

n = int(input())
cards = deque(range(1,n+1))
card_list = []

while cards : 
    a = cards.popleft()
    card_list.append(a)
    if cards :  
        a = cards.popleft()
        cards.append(a)

print(*card_list)