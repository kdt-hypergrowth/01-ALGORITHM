list_ = []

for i in range(10):
    n = int(input())
    n %= 42
    n = int(n)

    if n not in list_:
        list_.append(n)

print(len(list_))