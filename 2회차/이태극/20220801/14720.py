# 0은 딸기우유만을 파는 가게, 
# 1은 초코우유만을 파는 가게, 
# 2는 바나나우유만을 파는 가게를 뜻하며, 
# 맨 처음에는 딸기우유를 한 팩 마신다.
# 딸기우유를 한 팩 마신 후에는 초코우유를 한 팩 마신다.
# 초코우유를 한 팩 마신 후에는 바나나우유를 한 팩 마신다.
# 바나나우유를 한 팩 마신 후에는 딸기우유를 한 팩 마신다. 

n = int(input())
a = list(map(int, input().split()))

count = 0

for i in range(n):
    if a[i] == count % 3:
        count +=  1

print(count)