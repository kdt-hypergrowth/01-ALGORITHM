# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3회차/임선주/20220725/3_OX퀴즈.txt")

t = int(input())
answer = str(input())
answer1 = list(answer)
cnt = 0
result = 0
# print(len(answer))
# print(answer1[0])
for test_case in range(len(answer)+1):
    if answer1[test_case] == 'O':
        cnt += 1
        # print(cnt)
        if cnt != 0:
            result += cnt
            print(result)
        # print(result)
    else:
        cnt = 0
# print(result)




