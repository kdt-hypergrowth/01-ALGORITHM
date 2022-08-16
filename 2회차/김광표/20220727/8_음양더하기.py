# https://school.programmers.co.kr/learn/courses/30/lessons/76501
# 프로그래머스 음양 더하기 Lv2



def solution(absolutes, signs):
    for i in range(len(absolutes)) : 
        if signs[i] == False : # signs의 인덱스를 검사해 F일때만 음수로 바꿔준다.
            absolutes[i] *= -1

    answer = sum(absolutes) # sum함수로 합을 구해준다
    return answer

absolutes = [4,7,12]
signs = [True,False,True]

print(solution(absolutes, signs))