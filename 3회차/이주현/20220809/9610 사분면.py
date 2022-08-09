#https://www.acmicpc.net/problem/9610

# N = int(input())

# Q1= 0
# Q2= 0
# Q3= 0
# Q4= 0
# AXIS = 0

# for i in range(N):
#     x,y = map(int,input().split())
#     if x > 0 and y > 0 :
#         Q1 += 1
#     elif x < 0 and y > 0 :
#         Q2 += 1
#     elif x < 0 and y < 0 :
#         Q3 += 1
#     elif x > 0 and y < 0 :
#         Q4 += 1
#     else:
#         AXIS += 1


# print("Q1: ",Q1)
# print("Q2: ",Q2)
# print("Q3: ",Q3)
# print("Q4: ",Q4)
# print("AXIS: ",AXIS)


n = int(input())
axis = 0
q1 = 0
q2 = 0
q3 = 0
q4 = 0

for _ in range(n) :
  x, y = map(int, input().split())
  
  if x == 0 or y == 0 :
    axis += 1
  elif x > 0 and y > 0 :
    q1 += 1
  elif x < 0 and y > 0 :
    q2 += 1
  elif x < 0 and y < 0 :
    q3 += 1
  else :
    q4 += 1

print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)
print("Q4:", q4)
print("AXIS:", axis)
