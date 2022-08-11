T = int(input())
for test_case in range(T) : 
    car = int(input())
    option = int(input())
    price = car

    for _ in range(option) : 
        q, p = map(int,input().split())
        price += q * p
    
    print(price)