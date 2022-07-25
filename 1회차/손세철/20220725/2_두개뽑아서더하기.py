# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):

    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
# for를 사용해 이중 반복문을 만들어서 서로 다른 두개의 숫자 뽑아냄
            answer.append(numbers[i]+numbers[j])
    answer = sorted(list(set(answer)))
# i,j 합친 뒤 set으로 중복 제거, sorted로 오름차순으로 정렬

    return answer
print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))

