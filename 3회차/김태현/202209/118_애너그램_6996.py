import sys
sys.stdin = open("118_애너그램_6996.txt", "r")

tc = int(input())

for _ in range(tc):
    a, b = input().split()
    na = sorted(a)
    nb = sorted(b)

    if na == nb:
        print(f"{a} & {b} are anagrams.")
    else:
        print(f"{a} & {b} are NOT anagrams.")
