# https://www.acmicpc.net/problem/25192

N = 7
gom = 0
log_list = [
    'ENTER',
    'pjshwa',
    'chansol',
    'chogahui05',
    'ENTER',
    'pjshwa',
    'chansol'
]
# list_ = list()
set_ = set()
for log in log_list:
    if log == 'ENTER':
        set_.clear()

    else:
        # 닉네임 = log
        # list에서 중복을 탐색할 경우 : N만큼의 시간이 필요하다.
        # set에서 중복을 탐색할 경우 : 1만큼의 시간이 필요하다.
        if log not in set_:
            set_.add(log)
            gom += 1

print(gom)
