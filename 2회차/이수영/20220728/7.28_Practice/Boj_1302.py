import sys

sys.stdin = open("1302_input.txt")

n = int(input())
book_list = {}
for _ in range(n):
    name = input()
    if name in book_list:
        book_list[name] += 1
    else:
        book_list[name] = 1
max = 0
sbook = dict(sorted(book_list.items()))
for i in sbook:
    if(sbook[i]) > max:
        max = sbook[i]
        maxi = i
print(maxi)
print(sbook)
 #   sorted(a.key(), reverse=True)


