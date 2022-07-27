
ans = 0
score = 0
for i in range(10):
    mushroom = int(input())
    score += mushroom
    if 100 - ans >= abs(100-score):
        ans = score

print(ans)

