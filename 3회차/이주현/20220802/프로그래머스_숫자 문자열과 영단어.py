def solution(s):
    answer = s 
    num_s = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    #dictionary 에서 item 함수를 사용하면 딕셔너리에 있는 키와 값들의 쌍을 얻을 수 있다.
    for i in num_s.items():
        answer = answer.replace(i[0], str(i[1]))
                                                    


    return int(answer)