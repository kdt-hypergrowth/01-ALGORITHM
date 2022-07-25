# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
   
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    answer = set(answer)  # 중복제거
    return sorted(answer)  # 오름차순 정렬 
 

print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
