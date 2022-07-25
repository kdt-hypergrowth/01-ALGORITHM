'''
* 문제 : 배열을 입력받아 서로 다른 인덱스의 두 수를 더한 배열의 오름차순 정렬 
* 접근
    * 배열의 모든 요소에 대한 합으로 배열 만듬
    * 중복 제거 후 만든 배열의 오름차순 정렬
* 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/68644
'''

def solution(numbers):
    answer = []
    # 서로 다른 두 요소의 합으로 이루어진 list 작성
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    # 중복 제거 후 오름차순 정렬
    answer = list(set(answer))
    answer.sort()
    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))  

