from pprint import pprint

matrix = []
for _ in range(8) : 
    line = input()
    matrix.append(line)
# pprint(matrix)
horse = 0
for i in range(8):
    for j in range(8) :
        # i + j 의 값이 짝수일때
        if (i+j) % 2 == 0 : 
            # F가 있으면 
            if matrix[i][j] == 'F' : 
                # horse +1 
                horse += 1 
print(horse)
