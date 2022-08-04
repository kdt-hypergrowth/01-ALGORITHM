#signs 참이면 absolutes 양수, 거짓이면 음수
def solution(absolutes, signs):
    result = 0 
# signs와 absolutes의 길이 같아서 for 문으로 작성
    for i in range(3):

# sings가 참일때 양수
        if signs [i] == True:
            result += absolutes[i]
# 그 외 거짓일때 음수 처리
        else:
            result -= absolutes[i]
#    result = sum(absolutes)
# 세 수의 합을 구하는거니 sum을 사용해줌 <==여기서 틀림
    return result