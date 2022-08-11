# 1. 입력 값(n) 받기
# 2. 결과를 담을 변수를 생성(result)
# 3. for문으로 1부터 n까지 모든 수를 계산해보며 분해합을 구한다.
# 4. 제일 먼저 계산된 값을 출력한다. 없을 때는 0을 출력

n = int(input())
result = 0 

for i in range(1, n+1) : 
    nums = list(map(int, str(i))) #i값을 각 자릿수로 슬라이싱하여 리스트로 만든다
    result = sum(nums) + i #i라는 수와 i의 각 자릿수의 합 더하기
    if result == n : 
        print(i)
        break 
    if i == n :  #i가 분해합을 찾지 못하고 n까지 가게 된다면 분해합이 없는 것이므로 0을 출력
        print(0)