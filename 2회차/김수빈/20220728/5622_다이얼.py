word = input()
number = {'ABC': 2, 'DEF': 3, 'GHI': 4, 'JKL': 5,
            'MNO': 6, 'PQRS': 7, 'TUV': 8, 'WXYZ': 9}
time = 0

for i in word:
    time = number.get(i) + 1
    time += time

print(time)
