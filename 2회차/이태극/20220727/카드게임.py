# 4 5 6 7 0 1 2 3 9 8
# 1 2 3 4 5 6 7 8 9 0

a_scores = list(map(int,input().split()))
b_scores = list(map(int,input().split()))
a_point = b_point = 0
last = 'D'
for a_score, b_score in zip(a_scores, b_scores):
  if a_score > b_score:
    last = 'A'
    a_point += 3
  elif a_score < b_score:
    last = 'B'
    b_point += 3
  else:
    a_point += 1
    b_point += 1
print(a_point, b_point)
if a_point > b_point:
  print("A")
elif b_point < a_point:
  print("B")
else:
  print(last)