import sys  

sys.stdin = open("2_크로아티아 알파벳.txt")

arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
str = input()

for a in arr:
    str = str.replace(a, '*')

print(len(str))