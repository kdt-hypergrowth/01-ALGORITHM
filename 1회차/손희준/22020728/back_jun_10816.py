n = int(input())
dic = {}

card = list(input().split())
    
for j in card:
    if j in dic:
        dic[j] += 1
    else:
        dic[j] = 1

result = {}

m = int(input())

card_cnt = list(input().split())
for k in card_cnt:
    if k == dic[k]:
        result.get[k,'0']

print(result)