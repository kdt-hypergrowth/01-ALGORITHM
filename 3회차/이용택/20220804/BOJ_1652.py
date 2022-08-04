'''
Q. 누울 자리를 찾아라
'''
import sys

input = sys.stdin.readline

case = [list(input().rstrip()) for _ in range(int(input()))]

# new_list = list(map(list, zip(*mylist)))
transpose_case = list(map(list, zip(*case)))

row_cnt = 0
col_cnt = 0

for i in range(len(case)):
    check = 0

    for j in range(len(case[i])):
        if case[i][j] == '.':
            check += 1
        else:
            if check >= 2:
                row_cnt += 1
                check = 0
            else:
                check = 0
    if check >= 2:
        row_cnt += 1

for i in range(len(transpose_case)):
    check = 0
    for j in range(len(transpose_case[i])):
        if transpose_case[i][j] == '.':
            check += 1
        else:
            if check >= 2:
                col_cnt += 1
                check = 0
            else:
                check = 0
    if check >= 2:
        col_cnt += 1

print(row_cnt, col_cnt)