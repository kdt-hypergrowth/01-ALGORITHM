# 2753.
""" 
"""
year = int(input())
answer = 0
if year % 4 == 0:
    if not (year % 100 == 0):
       answer = 1
       
    elif year % 400 == 0:
        answer = 1
    
print(answer)
        