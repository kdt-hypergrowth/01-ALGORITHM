#https://www.acmicpc.net/problem/1526

N = int(input())   # 4<= N <= 1000000

while True:
    if len(str(N))==str(N).count('4')+ str(N).count('7'):
        print(N)
        break
        N -= 1    
    

