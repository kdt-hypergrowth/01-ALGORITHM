#https://www.acmicpc.net/problem/2587

my_list = []

for i in range(5):
    my_list.append(int(input()))


avg = sum(my_list) // 5

my_list.sort()
print(avg)
print(my_list[2])

