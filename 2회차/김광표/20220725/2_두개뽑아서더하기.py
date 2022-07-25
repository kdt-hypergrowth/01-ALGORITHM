# 두 개 뽑아서 더하기 Lv.1

def solution(numbers):
    answer = []
    for i in range(0,len(numbers)-1) :
        for j in range(i+1, len(numbers)) :  #각 인덱스를 모두 한번 씩 더해주었다.
            answer.append(numbers[i]+numbers[j])

    answer = list(set(answer)) # set를 이용해 중복을 제거하고, list로 만들었다.
    answer.sort() # sort로 순서대로 정렬해주었다.
    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5,0,2,7]))
