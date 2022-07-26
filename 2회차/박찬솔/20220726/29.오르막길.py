import sys

sys.stdin = open("29_오르막길.txt")

N = int(input())
arr = list(map(int,(input().split())))
    
temp = arr[0] ; sum = 0
answer = []
    
for i in range(1,N):
    if arr[i] - temp >0 : #더 높은 숫자가 등장시에, 그 차이를 sum에 더하기. 
        sum += arr[i]-temp
        temp = arr[i] # 현재 수(temp) 업데이트            
    elif arr[i] == temp or arr[i]-temp<0 : #같은수 또는 더 낮은 수가 등장시에
        answer.append(sum) #오르막길이 끝났으므로 방금까지의 오르막높이 sum을 list(answer)에 추가
        temp = arr[i] # 현재 수(temp) 업데이트
        sum = 0 #sum 초기화           
answer.append(sum) # 맨 마지막에 오르막길이 등장하면 위 for문으로는 append가 안되서 추가.
if len(answer) == 0 : print(0) # 오르막이 한번도 없었다면 0 출력
else : print(max(answer))