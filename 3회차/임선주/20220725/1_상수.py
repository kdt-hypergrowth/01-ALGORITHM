# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("3회차/임선주/20220725/1_상수.txt")

# a, b = map(int, input().split())
# result_a = int(str(a)[::-1])
# result_b = int(str(b)[::-1])
# # print(result_a, type(result_a))
# # print(result_b, type(result_b))
# result_list = [result_a, result_b]
# max_number = result_list[0]
# # print(result_list, type(result_list))
# # print(max_number)
# for number in range(2):
#     if result_list[number] > max_number:
#         max_number = result_list[number]
# print(max_number)

a, b = input().split()
a1 = int(a[::-1])
b1 = int(b[::-1])

if a1 > b1:
    print(a1, type(a1))
else:
    print(b1, type(b1))

print(a1) if a1 > b1 else print(b1)