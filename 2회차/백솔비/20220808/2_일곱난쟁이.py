import sys
sys.stdin = open("2_일곱난쟁이.txt")

dwarf = []
for _ in range(9):
    dwarf.append(int(input()))
dwarf.sort()

sum_ = sum(dwarf)
minus = sum_ - 100

for i in range(8):
    for j in range(i+1, 9):
        if dwarf[i] + dwarf[j] == minus:
            dwarf1, dwarf2 = i, j

for i in range(9):
    if i != dwarf1 and i != dwarf2:
        print(dwarf[i])