#https://www.acmicpc.net/problem/2309

dwarfs = []
for i in range(9):  # 9명의 난쟁이를 입력받아  난쟁이 리스트에 추가한다.
    N = int(input())
    dwarfs.append(N)

dwarfs.sort()       # 오름차순 정렬
total = sum(dwarfs)   # 난쟁이들의 키의 합 = total

for i in range(9):  # for 문을 7개 구현했다가 실패/ 9명 중에 2명을 비교후 빼기
    for j in range(i+1,9):      
        if total - (dwarfs[i] + dwarfs[j]) == 100:     # 전체 난쟁이 키에서난쟁이 1,2의 키의 합을 뺌 == 100?
            not_dwarfs1, not_dwarfs2 = dwarfs[i],dwarfs[j] # 1,2는 난쟁이 아님 변수에 지정

            dwarfs.remove(not_dwarfs1)      # 이후 난쟁이 리스트에서 제거
            dwarfs.remove(not_dwarfs2)

            for i in range(len(dwarfs)):    # 남은 7명의 진짜 난쟁이들을 출력
                print(dwarfs[i])

            break

    if len(dwarfs) == 7:        # 난쟁이 리스트에 7명이 남는다면 종료
        break



