# 소를 10마리 가지고 있으므로 소의 번호는 1 이상 10 이하의 정수고, 
# 소의 위치는 길의 왼쪽과 오른쪽을 의미하는 0과 1 중 하나다.

# 이 관찰 기록을 가지고 소가 최소 몇 번 길을 건넜는지 알아보자. 
# 즉 같은 번호의 소가 위치를 바꾼 것이 몇 번인지 세면 된다.
#---------------------------------------------------------

# 첫째 줄에 관찰횟수 n
n = int(input())
# 소의 번호, 위치를 저장할 딕셔너리 선언 
dic = {}
# 소가 길을 건넌 횟수를 셀 변수 선언
cnt = 0 

# 관찰횟수만큼 반복문을 돌면서 소의 번호,위치 입력받기
for i in range(n) : 
    num, location = map(int,input().split())
    
    # 만약 소의 번호가 dic에 없으면 num, location (소의 번호, 위치)를 dic 저장
    if num not in dic : 
        dic[num] = location 
    
    # 소의 번호가 dic에 있으면 위치가 같은지 다른지 봐야함 
    else : 
        # 위치가 같지 않다면 길을 건넌것으로 cnt +1 해주고 dic에 저장 
        if dic[num] != location : 
            cnt += 1 
            dic[num] = location

print(cnt)
