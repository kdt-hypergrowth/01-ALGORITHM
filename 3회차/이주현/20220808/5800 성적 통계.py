#https://www.acmicpc.net/problem/5800

K = int(input())

for i in range(K):

    grade = list(map(int,input().split()))
    del grade[0]        # 개수로 받은 맨 처음 리스트 삭제
    grade.sort()            # 오름차순 정렬, sorted()는 새로운 정렬된 리스트를 반환해주는 함수, sort()는 리스트 자체 정렬
    diff = []
    print('Class',i+1) # class 1~
    for i in range(len(grade)-1): # 받은 숫자 만큼 반복
        diff.append(grade[i+1]-grade[i]) # 오름차순 이기 때문에 (i+1) -i중 가장 큰 값을 최대차값으로 설정

    #print('Max',max(grade),', Min',min(grade),', Largest gap ', max(diff)) 내가 한  print

    print('Max', str(max(grade))+',' ,'Min', str(min(grade))+',', 'Largest gap', max(diff)) # 정답 print

