import sys
sys.stdin = open("3_나는요리사다.txt")

score = []

for i in range(5):
    scores = sum(list(map(int, input().split())))
    score.append(scores)
    #score = [18, 17, 18, 19, 17]

print(score.index(max(score))+1, max(score))
