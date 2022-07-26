# 1292.
"""
1을 한 번, 2를 두 번, 3을 세 번, 이런식으로
1 2 2 3 3 3 4 4 4 4 5 .. 수열을 만들고
어느 일정한 구간을 주면 그 구간의 합을 구하는 것이다.

# 입력
첫째 줄에 구간의 시작과 끝을 나타내는 정수가 주어진다.
즉, 수열에서 A번째 숫자부터 B번째 숫자까지 합을 구하면 된다.

# 출력
첫 줄에 구간에 속하는 숫자의 합을 출력

# 접근
1. 수열의 범위를 어디까지인지 알 수 없으므로,
2. B번째 자리가 존재하는 수열을 만들기 위해 길이가 B인 수열을 만든다.
4. 1부터 B까지의 수열을 저장할 리스트를 만들고
5. 범위의 수가 바인딩 될 때마다 해당 숫자를 숫자만큼 더한 값을 추가한다.
6. 인덱스로 접근하여 범위 안에 바인딩 되는 값을 모두 더한다.

"""
# 입력값을 받아온다
A, B = map(int, (input().split()))
# 수열을 저장할 리스트를 만든다.
between = []
sum_ = 0
for i in range(1, B+1):
#     between += [int(str(i))] * i
#     # B번째의 자리가 확보되는 수열이 되면 수열을 그만 생성한다.
#     if len(between) == B:
#         break
# # A번째부터 B번째 인덱스의 범위를 순회한다.
# for idx in range(A-1, B):
#     # 순회하면서 만나는 숫자들을 모두 합한다.
#     sum_ += between[idx]
# print(len(between))
# print(sum_)
    for j in range(i):       
        between.append(i)
print(sum(between[A-1:B]))