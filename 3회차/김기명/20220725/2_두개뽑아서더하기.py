# https://school.programmers.co.kr/learn/courses/30/lessons/68644
ans = set()

def solution(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if j != i:           # number를 순회하도록 하니까 리스트에 1,1 이런식으로 서로다른 1이 있을때 두개가 합해지지않음 !!! 
                ans.add(numbers[j] + numbers[i])      # 그래서 단순 숫자가 아닌 리스트의 구성요소를 더하게 했음
    return list(ans)


print(solution([5, 0, 2, 7]))  # 테스트케이스중 2개가 틀렸다고나오는데 확인이 불가능함. 왜 틀렸을까