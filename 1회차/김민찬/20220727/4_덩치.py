T = int(input()) 
big = []
for a in range(T):
    w, h= map(int, input().split()) # 테스트 케이스 5명의 몸무게, 키 입력
    
    big.append((w, h)) #리스트 저장
    #big = [(55, 185), (58, 183), (88, 186), (60, 175), (46, 155)]
           #[0 ,  1]              

for i in big: # [(55, 185), (58, 183), (88, 186), (60, 175), (46, 155)] 순회
    
    number = 1 # 시작값 1 (등수)
               # 밑에 for문에서 각각 비교하여 덩치가 더 작은 요소에 +1씩 해서 등수를 정할 예정
               
    for j in big:
        if i[0] < j[0] and i[1] < j[1]:
            number += 1

print(number, end = ' ')
   #공백으로 이어출력 -> 2 2 1 2 5